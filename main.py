from src.parser import Parser

if __name__ == '__main__':
    parser = Parser()
    parser.build(build_lexer=True)

    with open('tests/resources/input/input_test9.txt', 'r') as f:
        data = f.read()

    print('Return: ', parser.parser.parse(data, tracking=True))

