import json

from src.parser import Parser

if __name__ == '__main__':
    parser = Parser(debug=False)
    parser.build(build_lexer=True)

    data = \
    """ 
    program teste9
    declare
        integer base, altura, area;
    begin
        read(base);
        read(altura);
        area := (base * altura) / 2;
        write(variable);
    end
    """

    parser.parse_data(data)

    # print('\n\nSymbol Table: ', json.dumps(parser.lexer.symbol_table.table, indent=4))
