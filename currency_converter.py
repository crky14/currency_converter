from converter import Converter


if __name__ == "__main__":
    #parse arguments
    converter = Converter()
    args = converter.parse_arguments()
    result = converter.change_currency(args.amount, args.input_currency, args.output_currency)
    print(converter.to_json(result))
