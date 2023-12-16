import ply.yacc as yacc
from src.lexer import Lexer
from src.utils import Error, get_context


class Parser:
    tokens = Lexer.tokens

    def __init__(self, debug=False):
        self.errors: list[Error] = []
        self.parser = None
        self.data = None
        self.debug = debug
        self.lexer = Lexer(self.errors, debug=self.debug)

    def id_exists(self, symbol, p):
        if not self.lexer.symbol_table.exists(symbol):
            self.errors.append(Error(f"Symbol '{symbol}' not declared", p.lexer.lineno, p.lexer.lexpos, 'semantic', self.data))
            print(self.errors[-1])

    def p_error(self, p):
        if not p:
            self.errors.append(Error("Unexpected end of input", 0, 0, 'parser', self.data))
        else:
            self.errors.append(Error(f"Syntax error on '{p.value}'",
                                     p.lineno, p.lexpos, 'parser', self.data))
        print(self.errors[-1])
        # print(f"debug: {self.errors[-1].__repr__()}")

    def parse_data(self, data):
        self.data = data
        self.lexer.data = data
        self.parser.parse(data, tracking=True)

    def build(self, build_lexer=False):
        self.parser = yacc.yacc(module=self)
        if build_lexer:
            self.lexer.build()

    def p_program(self, p):
        """program : PROGRAM ID body"""
        p[0] = ('program', p[2], p[3])

    def p_body(self, p):
        """body : DECLARE declaration_list BEGIN statement_list END"""
        p[0] = ('body', p[2], p[4])

    def p_declaration_list(self, p):
        """declaration_list : declaration SEMICOLON declaration_list
                            | empty"""
        if len(p) == 2:
            p[0] = []
        else:
            p[0] = [p[1]] + p[3]

    def p_declaration(self, p):
        """declaration : type identifier_list"""
        p[0] = ('declaration', p[1], p[2])
        for t in p[2]:
            if not self.lexer.symbol_table.exists(t):
                self.lexer.symbol_table.add(t, p.lexer.lexpos, p.lexer.lineno, p[1])
            else:

                self.errors.append(Error(f"Symbol {t} already declared", p.lexer.lineno, p.lexer.lexpos,
                                         f'semantic', self.data))
                print(self.errors[-1])

    def p_identifier_list(self, p):
        """identifier_list : ID COMMA identifier_list
                           | ID"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_type(self, p):
        """type : INTEGER
                | DECIMAL"""
        p[0] = p[1]

    def p_statement_list(self, p):
        """statement_list : statement SEMICOLON p_statement_list_single"""

    def p_statement_list_single(self, p):
        """p_statement_list_single : statement_list
                            | empty"""

    def p_statement(self, p):
        """statement :  if_statement
                | assign_statement
                | while_statement
                | do_while_statement
                | for_statement
                | read_statement
                | write_statement"""

    def p_assign_statement(self, p):
        """assign_statement : ID ASSIGN expression"""
        if p.slice[1].type == 'ID':
            self.id_exists(p[1], p)
        p[0] = ('assign_statement', p[1], p[3])

    def p_if_statement(self, p):
        """if_statement : IF condition THEN statement_list if_statement_aux"""

    def p_if_statement_aux(self, p):
        """if_statement_aux : END
                            | ELSE statement_list END"""

    def p_condition(self, p):
        """condition : expression"""
        p[0] = p[1]

    def p_do_while_statement(self, p):
        """do_while_statement : DO statement_list WHILE condition"""
        p[0] = ('do-while', p[2], p[4])

    def p_for_statement(self, p):
        """for_statement : FOR assign_statement TO expression DO statement_list END"""
        p[0] = ('for', p[2], p[4], p[6])

    def p_while_statement(self, p):
        """while_statement : WHILE condition DO statement_list END"""
        p[0] = ('while', p[2], p[4])

    def p_read_statement(self, p):
        """read_statement : READ LPAREN ID RPAREN"""
        # validates if the id is in the symbol table
        self.id_exists(p[3], p)
        p[0] = ('read', p[3])

    def p_write_statement(self, p):
        """write_statement : WRITE LPAREN writable RPAREN"""
        p[0] = ('write', p[3])

    def p_writable(self, p):
        """writable : expression
                    | SCONST"""
        p[0] = p[1]

    def p_expression(self, p):
        """expression : simple_expression expression_aux"""
        if len(p) == 2:
            p[0] = p[1]

    def p_expression_aux(self, p):
        """expression_aux : relop simple_expression
                    | empty"""

    def p_dual_expression(self, p):
        """dual_expression : LPAREN expression RPAREN"""

    def p_simple_expression(self, p):
        """simple_expression : tern
                            | dual_expression TERNAL simple_expression COLON simple_expression
                            | simple_expression addop tern"""

        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 6:
            p[0] = ('tern', p[1], p[3], p[5])
        else:
            p[0] = (p[2], p[1], p[3])

    def p_tern(self, p):
        """tern : factor_a
                | tern mulop factor_a"""

    def p_factor_a(self, p):
        """factor_a : factor 
                | NOT factor 
                | MINUS factor"""

    def p_factor(self, p):
        """factor : ID 
                | NUMBER 
                | dual_expression"""

        if len(p) == 2:
            if p.slice[1].type == 'ID':
                self.id_exists(p[1], p)
            p[0] = p[1]
        elif p[1] in ['-', 'NOT']:
            p[0] = (p[1], p[2])
        else:
            if p.slice[2].type == 'ID':
                self.id_exists(p[2], p)
            p[0] = p[2]

    def p_unary(self, p):
        """unary : MINUS
                 | NOT"""

    def p_relop(self, p):
        """relop : EQUAL
                 | GREATER
                 | GREATEREQUAL
                 | LESS
                 | LESSEQUAL
                 | LESSGREATER"""

    def p_addop(self, p):
        """addop : PLUS
                 | MINUS
                 | OR"""

    def p_mulop(self, p):
        """mulop : MULTI
                 | DIVIDE
                 | MOD
                 | AND"""

    def p_constant(self, p):
        """constant : NUMBER"""

    def p_empty(self, p):
        """empty :"""
