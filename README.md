# Python Currency Converter

Currency converter that converts currencies and prints out result
in cool `JSON` format and api which returns same JSON.

All currency exchange rates are collected from European Central Bank using https://exchangeratesapi.io/ API.

## Requirements

* python 3
* sqlite3

After cloning github repository all needed python modules can be found in requirments.txt.
Install them with command `pip3 install -r requirements.txt`

## Implementation

Instead of simple requesting needed exchange rate from API my implementation creates simple
relation database. Database is created on first execution of application and filled with newest 
exchange rates from European Central Bank.
Every exection of CLI application or request on API application checks conditions and update
new exchange rates if it is possible.

## Usage

### CLI application
```
./currency-converter.py
    [-h]
    --amount AMOUNT
    --input_currency INPUT_CURRENCY
    [--output_currency OUTPUT_CURRENCY]

-h, --help                            show this help message and exit
--amount AMOUNT                       amount to convert
--input_currency INPUT_CURRENCY       code or symbol of currency to convert from
--output_currency OUTPUT_CURRENCY     code or symbol of currency to convert to (optional)
```

### API

```
./currency-converter_api.py
```
 Running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) by default
   
 Example:
```
http://127.0.0.1:5000/currency_converter?amount=100&input_currency=EUR&output_currency=USD
```
   
  
### Supported currency symbol conversions

This table shows all supported currency symbols and corresponding currency.

| Currency symbol | Currency code | Currency name |
|-----|-----|------------------------|
| $   | USD | United States dollar   |
| Fr. | CHF | Swiss franc            |
| Ft  | HUF | Hungarian forint       |
| HK$ | HKD | Hong Kong dollar       |
| Kr  | DKK | Danish krone           |
| Kč  | CZK | Czech koruna           |
| L   | RON | Romanian leu           |
| NZ$ | NZD | New Zealand dollar     |
| R$  | BRL | Brazilian real         |
| R   | RUB | Russian ruble          |
| RM  | MYR | Malaysian ringgit      |
| Rp  | IDR | Indonesian rupiah      |
| S$  | SGD | Singapore dollar       |
| W   | KRW | South Korean won       |
| kn  | HRK | Croatian kuna          |
| kr  | NOK | Norwegian krone        |
| zł  | PLN | Polish zloty           |
| £   | GBP | British pound          |
| ¥   | JPY | Japanese yen           |
| ฿   | THB | Thai baht              |
| ₪   | ILS | Israeli new sheqel     |
| €   | EUR | European Euro          |
| ₱   | PHP | Philippine peso        |
| ₹   | INR | Indian rupee           |
