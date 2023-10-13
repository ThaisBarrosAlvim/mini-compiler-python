from unittest import TestCase

from lexer import Lexer


class TestLexer(TestCase):

    INPUT_TESTS_FOLDER = 'resources/input'
    EXPECTED_TESTS_FOLDER = 'resources/expected'

    def setUp(self) -> None:
        self.lexer = Lexer()
        self.lexer.build()

    def lexer_proccess_data(self, input_file_path: str):
        data = self.read_file(input_file_path)
        self.lexer.lex.input(data)
        token_output = []
        while True:
            tok = self.lexer.lex.token()
            if not tok:
                break
            token_output.append(tok.type)
        return token_output

    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def test_lexer_test1(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test1.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test1.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test2(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test2.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test2.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test3(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test3.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test3.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test4(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test4.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test4.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test5(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test5.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test5.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test6(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test6.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test6.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test7(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test7.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test7.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test8(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test8.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test8.txt').split()
        self.assertEqual(expected, result)

    def test_lexer_test9(self):
        result = self.lexer_proccess_data(f'{self.INPUT_TESTS_FOLDER}/input_test9.txt')
        expected = self.read_file(f'{self.EXPECTED_TESTS_FOLDER}/expected_test9.txt').split()
        self.assertEqual(expected, result)
