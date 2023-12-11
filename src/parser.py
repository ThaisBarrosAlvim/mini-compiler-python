import ply.yacc as yacc
from src.lexer import Lexer


class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.errors = []
        self.parser = None
        self.data = None

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
        p[0] = ('assign_statement', p[1], p[3])

    def p_if_statement(self, p):
        """if_statement : IF condition THEN statement_list if_statement_aux"""

    def p_if_statement_aux(self, p):
        """if_statement_aux : END
                            | ELSE statement_list END"""

    def p_condition(self, p):
        """condition : expression"""
        # FIXME erro no teste5
        # p[0] = (p[2], p[1], p[3])

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
        p[0] = ('read', p[3])

    def p_write_statement(self, p):
        """write_statement : WRITE LPAREN writable RPAREN"""
        p[0] = ('write', p[3])

    def p_writable(self, p):
        """writable : expression
                    | SCONST"""

    def p_expression(self, p):
        """expression : simple_expression expression_aux"""
        # FIXME erro em todos
        # if len(p) == 2:
        #     p[0] = p[1]
        # else:
        #     p[0] = (p[2], p[1], p[3])

    def p_expression_aux(self, p):
        """expression_aux : relop simple_expression
                    | empty"""

    def p_par_expression(self, p):
        """par_expression : LPAREN expression RPAREN"""

    def p_simple_expression(self, p):
        """simple_expression : term
                            | par_expression TERNAL simple_expression COLON simple_expression
                            | simple_expression addop term"""

    def p_term(self, p):
        """term : factor_a
                | term mulop factor_a"""

    def p_factor_a(self, p):
        """factor_a : factor 
                | NOT factor 
                | MINUS factor"""

    def p_factor(self, p):
        """factor : ID 
                | NUMBER 
                | par_expression"""

        if len(p) == 2:
            p[0] = p[1]
        elif p[1] in ['-', 'NOT']:
            p[0] = (p[1], p[2])
        else:
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

    def p_error(self, p):
        if not p:
            self.errors.append("Parser: Syntax error at EOF")
        else:
            error_line = self.data.split('\n')[p.lineno-1]
            where = error_line.lstrip() + '\n' + " " * ((p.lexpos - len('\n'.join(self.data.split('\n')[:p.lineno-1]))) - ((len(error_line) - len(error_line.lstrip()))+1)) + "^"
            self.errors.append(f"Parser: Syntax error at line {p.lineno} token {p.type}. "
                               f"On:\n{where}")
        print(self.errors[-1])
        # print(f"debug: {self.errors[-1].__repr__()}")

    def build(self, build_lexer=False):
        self.parser = yacc.yacc(module=self)
        if build_lexer:
            Lexer().build()
