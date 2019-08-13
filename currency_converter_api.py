from flask import request, jsonify
from flask_api import FlaskAPI, status
from converter import Converter

app = FlaskAPI(__name__)


@app.route("/currency_converter", methods=['GET'])
def convert_currency():
    args = request.args
    amount = request.args.get("amount")
    input_currency = request.args.get("input_currency")
    output_currency = request.args.get("output_currency")
    error_response = {
        'error': "",
        'required arguemnts': {
            'amount': "Amount to exchange (float)",
            'input_currency': "Base currency (string)"
        },
        'optional arguments': {
            'output_currency': "Wanted currencies (string)"
        }
    }
    print(error_response)
    if amount == None or input_currency == None:
        error_response['error'] = "Request missing required argument"
        return jsonify(error_response), status.HTTP_400_BAD_REQUEST
    try:
        amount = float(amount)
    except:
        error_response['error'] = "Amount have to be a number"
        return jsonify(error_response), status.HTTP_400_BAD_REQUEST
    # convertion
    converter = Converter()
    result = converter.change_currency(amount, input_currency, output_currency)
    return jsonify(result), status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
