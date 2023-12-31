import os
from unittest import TestCase

from src.parser import Parser
from src.utils import Error
from tests.utils import read_file


class TestErrors(TestCase):
    BASE_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    INPUT_TESTS_FOLDER = f'{BASE_FILE_PATH}/resources/input'
    LEXER_DEBUG = False  # Set to True to see the lexer debug output

    def setUp(self) -> None:
        print(f'\n{self._testMethodName.center(45, "-")}\n')
        self.parser = Parser(self.LEXER_DEBUG)
        self.parser.build(build_lexer=True)

    def parser_proccess_data(self, input_file_path: str):
        data = read_file(input_file_path)
        self.parser.parse_data(data)

    def check_expected(self, input_file_path: str, expected_errors: list[Error]):
        self.parser_proccess_data(f'{self.INPUT_TESTS_FOLDER}/{input_file_path}')
        # print('\n\nErrors: \n',
        #       '\n'.join([e.exact().__repr__()[1:-1] for e in self.parser.errors]))
        self.assertEqual([e for e in self.parser.errors], expected_errors)

    def test_lexer_test1(self):
        errors = [
            Error("Syntax error on 'write'", line=10, column=156, _type='parser'),
        ]
        self.check_expected('input_test1.txt', errors)

    def test_lexer_test2(self):
        errors = [
            Error("Syntax error on 'declarando'", line=2, column=15, _type='parser')
        ]
        self.check_expected('input_test2.txt', errors)

    def test_lexer_test3(self):
        errors = [
            Error("Illegal character '#'", line=11, column=179, _type='lexer'),
            Error("Syntax error on 'id'", line=11, column=181, _type='parser')
        ]
        self.check_expected('input_test3.txt', errors)

    def test_lexer_test4(self):
        errors = [
            Error("Illegal character '_'", line=3, column=44, _type='lexer'),
            Error("Illegal character '$'", line=8, column=141, _type='lexer')
        ]
        self.check_expected('input_test4.txt', errors)

    def test_lexer_test5(self):
        errors = [
            Error("Syntax error on 'else'", line=10, column=142, _type='parser')
        ]
        self.check_expected('input_test5.txt', errors)

    def test_lexer_test6(self):
        errors = [
            Error("Syntax error on '>'", line=9, column=139, _type='parser')
        ]
        self.check_expected('input_test6.txt', errors)

    def test_lexer_test7(self):
        errors = [
            Error("Syntax error on '>'", line=9, column=143, _type='parser')
        ]
        self.check_expected('input_test7.txt', errors)

    def test_lexer_test8(self):
        errors = [
            Error("Symbol peso already declared", line=4, column=63, _type='semantic'),
            Error("Symbol 'altura' not declared", line=7, column=102, _type='semantic'),
            Error("Symbol 'altura' not declared", line=8, column=130, _type='semantic'),
            Error("Symbol 'altura' not declared", line=8, column=137, _type='semantic'),
        ]
        self.check_expected('input_test8.txt', errors)

    def test_lexer_test9(self):
        errors = [
            Error("Symbol 'variable' not declared", line=8, column=147, _type='semantic')
        ]
        self.check_expected('input_test9.txt', errors)
