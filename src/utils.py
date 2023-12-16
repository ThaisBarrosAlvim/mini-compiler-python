from typing import Literal


class Error:
    def __init__(self, message, line, column, _type: Literal['lexer', 'parser', 'semantic'], data=None):
        self.message = message
        self.line = line
        self.column = column
        self.type = _type
        self.data = data

    def __repr__(self):
        return (f"ERROR({self.type.upper()}): {self.message} at line {self.line}, column {self.column}"
                + (f". On:\n{get_context(self.data, self.line, self.column)}" if self.data else ""))

    def exact(self):
        return f"Error({self.message}, line={self.line}, column={self.column}, _type={self.type})"

    def __eq__(self, other):
        return (self.message == other.message and self.line == other.line and self.column == other.column
                and self.type == other.type)


def get_context(data, lineno, lexpos):
    error_line = data.split('\n')[lineno-1]
    where = error_line.lstrip() + '\n' + " " * ((lexpos - len('\n'.join(data.split('\n')[:lineno-1])))
                                                - ((len(error_line) - len(error_line.lstrip()))+1)) + "^"
    return where
