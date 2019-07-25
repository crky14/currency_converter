from database import Database, DatabaseException
import argparse
import json

class Converter(object):
    """docstring for CurrencyConverter."""

    def __init__(self):
        super(Converter, self).__init__()
        try:
            self.db = Database()
        except DatabaseException as e:
            print(e)

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--amount', type=float, required=True, help='Amount to exchange')
        parser.add_argument('-i', '--input_currency', required=True, help='Input currency three letter name or symbol')
        parser.add_argument('-o', '--output_currency', help='Output currency three letter name or symbol (If not specified, all will be used)')
        return parser.parse_args()

    def change_currency(self, amount, base, wanted=None):
        try:
            if(wanted == None):
                base_name, rates = self.db.get_rate(base)
            else:
                base_name, rates = self.db.get_rate(base, wanted)
        except DatabaseException as e:
            print(e)
            return None
        #create result dict
        result = {
            "input" : {
                "amount": amount,
                "currency": base_name
            },
            "output": {}
        }
        rates = [(i[0], format(i[1] * amount, '.2f')) for i in rates]
        result["output"].update(rates)
        return json.dumps(result, indent=4, sort_keys=True)
