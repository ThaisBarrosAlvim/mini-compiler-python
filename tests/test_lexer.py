import os
from unittest import TestCase

from src.lexer import Lexer
from tests.utils import read_file


class TestLexer(TestCase):

    BASE_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    INPUT_TESTS_FOLDER = f'{BASE_FILE_PATH}/resources/input'
    EXPECTED_TESTS_FOLDER = f'{BASE_FILE_PATH}/resources/expected/lexer'

    def setUp(self) -> None:
        self.lexer = Lexer()
        self.lexer.build()

    def lexer_proccess_data(self, input_file_path: str):
        data = read_file(input_file_path)
        self.lexer.lex.input(data)
        token_output = []
        while True:
            tok = self.lexer.lex.token()
            if not tok:
                break
            token_output.append(tok.type)
        return token_output

    def check_expected(self, input_file_path: str, expected_file_path: str):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/{input_file_path}')
        expected = read_file(f'{self.EXPECTED_TESTS_FOLDER}/{expected_file_path}').split()
        self.assertEqual(expected, result)

    def test_lexer_test1(self):
        self.check_expected('input_test1.txt', 'expected_test1.txt')

    def test_lexer_test2(self):
        self.check_expected('input_test2.txt', 'expected_test2.txt')

    def test_lexer_test3(self):
        self.check_expected('input_test3.txt', 'expected_test3.txt')

    def test_lexer_test4(self):
        self.check_expected('input_test4.txt', 'expected_test4.txt')

    def test_lexer_test5(self):
        self.check_expected('input_test5.txt', 'expected_test5.txt')

    def test_lexer_test6(self):
        self.check_expected('input_test6.txt', 'expected_test6.txt')

    def test_lexer_test7(self):
        self.check_expected('input_test7.txt', 'expected_test7.txt')

    def test_lexer_test8(self):
        self.check_expected('input_test8.txt', 'expected_test8.txt')

    def test_lexer_test9(self):
        self.check_expected('input_test9.txt', 'expected_test9.txt')
