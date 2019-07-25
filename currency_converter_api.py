from flask import request
from flask_api import FlaskAPI, status
from converter import Converter

app = FlaskAPI(__name__)

@app.route("/currency_converter", methods=['GET'])
def convert_currency():
    converter = Converter()
    args = request.args
    amount = request.args.get("amount")
    input_currency = request.args.get("input_currency")
    output_currency = request.args.get("output_currency")
    if(amount == None or input_currency == None):
        return "Request missing required arguments", status.HTTP_400_BAD_REQUEST
    try:
        amount = float(amount)
    except:
        return "Amount have to be number", status.HTTP_400_BAD_REQUEST
    #converion
    convertion = converter.change_currency(amount, input_currency, output_currency)
    if(convertion == None):
        return "Unsupported currency", status.HTTP_400_BAD_REQUEST
    else:
        return convertion, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True)
