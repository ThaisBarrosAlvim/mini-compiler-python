from lexer import Lexer
from ply import lex

lexer = Lexer()
lexer.build()

if __name__ == "__main__":
    lex.runmain(lexer.lex)
