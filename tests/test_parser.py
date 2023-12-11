import os
from unittest import TestCase

from src.parser import Parser
from tests.utils import read_file


class TestParser(TestCase):
    BASE_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    INPUT_TESTS_FOLDER = f'{BASE_FILE_PATH}/resources/input'

    def setUp(self) -> None:
        print(f'\n{self._testMethodName}\n\n')
        self.parser = Parser()
        self.parser.build(build_lexer=True)

    def parser_proccess_data(self, input_file_path: str):
        data = read_file(input_file_path)
        self.parser.data = data
        self.parser.parser.parse(data)

    def check_expected(self, input_file_path: str, expected: str | None):
        self.parser_proccess_data(f'{self.INPUT_TESTS_FOLDER}/{input_file_path}')
        self.assertEqual(self.parser.errors[-1] if len(self.parser.errors) > 0 else None, expected)

    def test_lexer_test1(self):
        self.check_expected('input_test1.txt', 'Parser: Syntax error at line 10 token WRITE. On:\nwrite(result)\n^')

    def test_lexer_test2(self):
        self.check_expected('input_test2.txt', 'Parser: Syntax error at line 2 token ID. On:\ndeclarando\n^')

    def test_lexer_test3(self):
        self.check_expected('input_test3.txt', 'Parser: Syntax error at line 11 token ID. On:\nsoma := soma # id;\n               ^')

    def test_lexer_test4(self):
        self.check_expected('input_test4.txt', None)

    def test_lexer_test5(self):
        self.check_expected('input_test5.txt', 'Parser: Syntax error at line 10 token ELSE. On:\nelse\n^')

    # def test_lexer_test6(self):
    #     # TODO validar onde eh o erro
    #     self.check_expected('input_test6.txt', 'Parser: Syntax error at line 9 position 131 token GREATER')
    #
    # def test_lexer_test7(self):
    #     # TODO validar onde eh o erro
    #     self.check_expected('input_test7.txt', 'Parser: Syntax error at line 9 position 135 token GREATER')

    def test_lexer_test8(self):
        self.check_expected('input_test8.txt', None)

    def test_lexer_test9(self):
        self.check_expected('input_test9.txt', None)
