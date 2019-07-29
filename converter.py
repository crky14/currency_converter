import argparse
import json
import requests

class Converter(object):
    """docstring for CurrencyConverter."""
    url_api = "https://api.exchangeratesapi.io/latest?base={}&symbols={}"

    currencies = {
        '€':	'EUR',
        'US$':  'USD',
        'JP¥':	'JPY',
        'лв' :	'BGN',
        'Kč' :  'CZK',
        'Dkr':	'DKK',
        '£':	'GBP',
        'Ft':	'HUF',
        'zł':	'PLN',
        'lei':	'RON',
        'Skr':	'SEK',
        'Fr':	'CHF',
        'Ikr':	'ISK',
        'Nkr':	'NOK',
        'kn':	'HRK',
        'R':	'RUB',
        'TRY':	'TRY',
        'AU$':	'AUD',
        'R$':	'BRL',
        'CA$':	'CAD',
        'CN¥':	'CNY',
        'HK$':	'HKD',
        'Rp':	'IDR',
        '₪':	'ILS',
        '₹':	'INR',
        'W':	'KRW',
        'Mx$':  'MXN',
        'RM':	'MYR',
        'NZ$':	'NZD',
        '₱':	'PHP',
        'S$':	'SGD',
        '฿':	'THB',
        'R':	'ZAR'
    }

    def __init__(self):
        super(Converter, self).__init__()

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--amount', type=float, required=True, help='Amount to exchange')
        parser.add_argument('-i', '--input_currency', required=True, help='Input currency three letter name or symbol')
        parser.add_argument('-o', '--output_currency', help='Output currency three letter name or symbol (If not specified, all will be used)')
        return parser.parse_args()

    def change_currency(self, amount, base, wanted=None):
        #check for currency sign
        if base in self.currencies.keys():
            base = self.currencies[base]
        if wanted == None:
            wanted = ''
        else:
            if wanted in self.currencies.keys():
                wanted = self.currencies[wanted]
        #api call
        response = requests.get(self.url_api.format(base, wanted))
        response_data = json.loads(response.text)
        if response.status_code == requests.codes.ok:
            #create result dict
            result = {
                "input" : {
                    "amount": amount,
                    "currency": response_data['base']
                },
                "output": {}
            }
            rates = response_data['rates']
            rates = [(key, format(value * amount, '.2f')) for key, value in response_data['rates'].items()]
            result["output"].update(rates)
            return result
        #convertion failed
        return response_data

    def to_json(self, dict):
        return json.dumps(dict, indent=4, sort_keys=True)
