import sqlite3
import os
import requests
import json
from datetime import datetime, date

class Database(object):
    """docstring for Database."""

    currencies = {
        'EUR': '€',
        'USD': 'US$',
        'JPY': 'JP¥',
        'BGN': 'лв',
        'CZK': 'Kč',
        'DKK': 'Dkr',
        'GBP': '£',
        'HUF': 'Ft',
        'PLN': 'zł',
        'RON': 'lei',
        'SEK': 'Skr',
        'CHF': 'Fr',
        'ISK': 'Ikr',
        'NOK': 'Nkr',
        'HRK': 'kn' ,
        'RUB': 'R',
        'TRY': 'TRY',
        'AUD': 'AU$',
        'BRL': 'R$',
        'CAD': 'CA$',
        'CNY': 'CN¥',
        'HKD': 'HK$',
        'IDR': 'Rp',
        'ILS': '₪',
        'INR': '₹',
        'KRW': 'W',
        'MXN': 'Mex$',
        'MYR': 'RM',
        'NZD': 'NZ$',
        'PHP': '₱',
        'SGD': 'S$',
        'THB': '฿',
        'ZAR': 'R'
    }
    database_dir = './database'
    database_path = './database/currency_database.db'
    url_api = 'https://api.exchangeratesapi.io/latest'

    def __init__(self):
        super(Database, self).__init__()
        #create connection to database
        if not os.path.exists(self.database_dir):
            os.makedirs(self.database_path)
        try:
            self.connection = sqlite3.connect(self.database_dir+'/currency_database.db')
        except:
            raise DatabaseException("Could not connect do database")
        #check database
        self.create_tables()
        self.init_database()

    def __del__(self):
        self.connection.close()

    def create_tables(self):
        cur = self.connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS dates (id INTEGER PRIMARY KEY,
                                                        last_update DATE NOT NULL);""")

        cur.execute("""CREATE TABLE IF NOT EXISTS currencies (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            name TEXT NOT NULL CHECK (length(name) == 3),
                                                            sign TEXT NOT NULL CHECK (length(sign) <= 4));""")

        cur.execute("""CREATE TABLE IF NOT EXISTS rates (input_currency_id INTEGER NOT NULL,
                                                            output_currency_id INTEGER NOT NULL,
                                                            rate FLOAT NOT NULL,
                                                            FOREIGN KEY(input_currency_id) REFERENCES currencies(id),
                                                            FOREIGN KEY(output_currency_id) REFERENCES currencies(id),
                                                            PRIMARY KEY(input_currency_id, output_currency_id));""")
        self.connection.commit()

    def init_database(self):
        cur = self.connection.cursor()
        cur.execute("""SELECT * FROM currencies""")
        results = cur.fetchall()
        if(len(results) == 0):
            insert_query = """INSERT INTO currencies (name, sign) VALUES (?, ?);"""
            values = []
            for code, sign in self.currencies.items():
                values.append((code, sign))
            cur.executemany(insert_query, values)
            self.connection.commit()
            self.update_rates()

    def update_rates(self):
        #update time
        response = requests.get(self.url_api)
        if(response.status_code == requests.codes.ok):
            date = json.loads(response.text)['date']
            self.insert_date(date)
        #update rates
        for code in self.currencies.keys():
            response = requests.get(self.url_api + '?base=' + code)
            if(response.status_code == requests.codes.ok):
                dict = json.loads(response.text)
                self.insert_rates(dict)

    def insert_date(self, value):
        cur = self.connection.cursor()
        cur.execute("""INSERT OR REPLACE INTO dates (id, last_update) VALUES (1, ?);""", (self.convert_date(value),))
        self.connection.commit()

    def convert_date(self, value):
        values = value.split('-')
        return date(int(values[0]), int(values[1]), int(values[2]))

    def insert_rates(self, dict):
        cur = self.connection.cursor()
        insert_query = """INSERT OR REPLACE INTO rates (input_currency_id, output_currency_id, rate)
                        SELECT a.id, b.id, ? FROM currencies AS a, currencies AS b
                        WHERE a.name=? AND b.name=?;"""
        base = dict['base']
        for key, value in dict['rates'].items():
            cur.execute(insert_query, (value, base, key))
        self.connection.commit()

    def get_rate(self, base, wanted=None):
        cur = self.connection.cursor()
        cur.execute("""SELECT last_update FROM dates;""")
        result = cur.fetchone()
        if(result == None):
            self.update_rates()
        else:
            last_date = self.convert_date(result[0])
            today = date.today()
            time = datetime.now()
            timedif = today - last_date
            if(timedif.days > 1 or last_date < today and time.hour >= 18):
                self.update_rates()

        cur.execute("""SELECT name FROM currencies WHERE name=? or sign=?""", (base, base))
        base_name = cur.fetchone()
        if(base_name == None):
            raise DatabaseException("Unsupported input currency")

        select_all_query = """SELECT name, rate FROM rates
                                JOIN currencies
                                ON currencies.id == rates.output_currency_id
                                WHERE rates.input_currency_id IN (SELECT id FROM currencies WHERE name=? or sign=?);"""

        select_single_query = """SELECT name, rate FROM rates
                                JOIN currencies
                                ON currencies.id == rates.output_currency_id
                                WHERE rates.input_currency_id IN (SELECT id FROM currencies WHERE name=? or sign=?)
                                AND rates.output_currency_id IN (SELECT id FROM currencies WHERE name=? OR sign=?);"""

        #select rate
        if(wanted == None):
            cur.execute(select_all_query, (base,base))
        else:
            cur.execute(select_single_query, (base, base, wanted, wanted))
        result = cur.fetchall()
        if(len(result) == 0):
            raise DatabaseException("Unsupported output currency")
        return base_name[0], result


'''Custom database exception'''
class DatabaseException(Exception):
    pass
