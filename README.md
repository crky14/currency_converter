# Python Currency Converter

Currency converter that converts currencies and prints out result
in cool `JSON` format and api which returns same JSON.

All currency exchange rates are collected from European Central Bank using https://exchangeratesapi.io/ API.

## Requirements

* python3

After cloning github repository all needed python modules can be found in requirments.txt.
Install them with command 
```pip3 install -r requirements.txt```

## Implementation

Application get exchange rates from European Central Bank by consuming API request created from arguments.
Rates are used to create demanded exchange to needed currency.

## Usage

### CLI application
```
./currency-converter.py
    [-h]
    -a OR --amount AMOUNT
    -i OR --input_currency INPUT_CURRENCY
    [-o OR --output_currency OUTPUT_CURRENCY]

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
   
 Examples:
```
http://127.0.0.1:5000/currency_converter?amount=100&input_currency=EUR&output_currency=USD

http://127.0.0.1:5000/currency_converter?amount=50&input_currency=CA$
```
   
  
### Supported currencies and their symbols

This table shows all supported currencies and their symbols/signs.

| Currency symbol | Currency code | Currency name |
|-----|-----|---------------------------|
|  €  | EUR |   Euro                    |
| US$ | USD |	US dollar               |
| JP¥ | JPY |	Japanese yen            |
| лв  | BGN |	Bulgarian lev           |
| Kč  | CZK |	Czech koruna            |
| Dkr | DKK |	Danish krone            |
|  £  | GBP |	Pound sterling          |
| Ft  | HUF |	Hungarian forint        |
| zł  | PLN |	Polish zloty            |
| lei | RON |	Romanian leu            |
| Skr | SEK |	Swedish krona           |
| Fr  | CHF |	Swiss franc             |
| Ikr | ISK |	Icelandic krona         |
| Nkr | NOK |	Norwegian krone         |
| kn  | HRK |	Croatian kuna           |
|  R  | RUB |	Russian rouble          |
| TRY | TRY |	Turkish lira            |
| AU$ | AUD |	Australian dollar       |
| R$  | BRL |	Brazilian real          |
| CA$ | CAD |	Canadian dollar         |
| CN¥ | CNY |	Chinese yuan renminbi   |
| HK$ | HKD |	Hong Kong dollar        |
| Rp  | IDR |	Indonesian rupiah       |
|  ₪  | ILS |	Israeli shekel          |
|  ₹  | INR |	Indian rupee            |
|  W  | KRW |	South Korean won        |
| Mx$ | MXN |	Mexican peso            |
| RM  | MYR |	Malaysian ringgit       |
| NZ$ | NZD |	New Zealand dollar      |
|  ₱  | PHP |	Philippine peso         |
| S$  | SGD |	Singapore dollar        |
|  ฿  | THB |	Thai baht               |
|  R  | ZAR |	South African rand      |

