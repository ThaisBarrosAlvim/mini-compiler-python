class SymbolTable:

    def __init__(self):
        self.table = {}

    def __str__(self):
        return str(self.table)

    def add(self, symbol, pos, line, tk_type=None):
        if symbol not in self.table:
            self.table[symbol] = {"Position": {"line": line, "pos": pos}, "Type": tk_type}
        else:
            raise Exception(f"{symbol} has already been declared")

    def exists(self, symbol):
        return symbol in self.table

    def get(self, symbol):
        if symbol in self.table:
            return self.table[symbol]
        else:
            raise Exception(f"{symbol} has not been declared")

    def remove(self, symbol):
        del self.table[symbol]
