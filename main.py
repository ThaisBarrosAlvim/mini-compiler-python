import json

from src.parser import Parser

if __name__ == '__main__':
    parser = Parser(debug=False)
    parser.build(build_lexer=True)

    with open('tests/resources/input/input_test6.txt', 'r') as f:
        data = f.read()
    parser.parse_data(data)
    print('\n\ntabela de simbolos: ', json.dumps(parser.lexer.symbol_table.table, indent=4))
