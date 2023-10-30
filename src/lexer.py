import ply.lex as lex

from src.symbol_table import SymbolTable


class Lexer:
    def __init__(self):
        self.lex = None
        self.symbol_table = SymbolTable()
        self.reserved_map = {}
        for r in self.reserved:
            self.reserved_map[r.lower()] = r

    reserved = (
        'IF', 'ELSE', 'THEN', 'WHILE', 'FOR', 'DO', 'TO', 'READ', 'WRITE', 'PROGRAM', 'DECLARE', 'INTEGER', 'DECIMAL',
        'BEGIN', 'END', 'AND', 'OR', 'NOT', 'MOD',
    )

    tokens = reserved + (
        # Literals (identifier, integer constant, float constant, string constant, char const)'ID',
        'ID', 'NUMBER', 'SCONST',

        # Operators (+,-,*,/,%,<,>,<=,>=,==,!=,&&,||,!,=)
        'PLUS', 'MINUS', 'MULTI', 'DIVIDE', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 'COLON', 'EQUAL', 'LESS',
        'LESSEQUAL', 'GREATER', 'GREATEREQUAL', 'ASSIGN', 'DOT', 'DOUBLEGREATER', 'DOUBLELESS', 'TRIPLELESS',
        'TRIPLEGREATER', 'LESSGREATER', 'TERNAL', 'LITERAL'
    )

    # Regular expression rules for simple tokens

    # Operators
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MULTI = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_EQUAL = r'='
    t_LESS = r'<'
    t_GREATER = r'>'
    t_ASSIGN = r':='
    t_DOT = r'\.'
    t_DOUBLEGREATER = r'>>'
    t_DOUBLELESS = r'<<'
    t_TRIPLELESS = r'<<<'
    t_TRIPLEGREATER = r'>>>'
    t_LESSGREATER = r'<>'
    t_TERNAL = r'\?'

    # String literal
    t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

    t_ignore = ' \t'

    def t_ID(self, t):
        r"""[a-zA-Z_][a-zA-Z_0-9]*"""
        t.type = self.reserved_map.get(t.value, 'ID')
        if t.type == 'ID':
            if not self.symbol_table.exists(t.value):
                self.symbol_table.add(t.value, t.lexpos, t.lineno, t.type)
        return t

    def t_NUMBER(self, t):
        r"""\d+"""
        t.value = int(t.value)
        return t

    def t_DECIMAL(self, t):
        r"""\d+\.\d+"""
        t.value = float(t.value)
        return t

    def t_LITERAL(self, t):
        r"""\"[^"]*\\"""
        return t

    def t_NEWLINE(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_COMMENT(self, t):
        r"""\%.*"""
        pass

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, ):
        self.lex = lex.lex(module=self)
