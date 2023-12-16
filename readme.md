# Lexical, Syntax, and Semantic Analyzer with PLY

This project is a comprehensive analyzer for a programming language, using Python and the PLY library. It includes lexical, syntax, and semantic analysis, with custom tokens, processing rules, a symbol table, and error handling.

## Project Overview

The analyzer comprises lexical, syntax, and semantic components. It's built using PLY (Python Lex-Yacc), facilitating the construction of lexer and parser for source code analysis. The semantic analyzer is integrated with the syntactic analyzer for validating semantic errors during compilation.

### Key Features

- **Lexical Analyzer**: Groups source code into lexemes and tokens.
- **Syntax Analyzer**: Validates the token stream against the programming language's syntax.
- **Semantic Analyzer**: Ensures instructions are semantically coherent for machine language conversion.

## Requirements

- Python 3.x
- [PLY library](https://github.com/dabeaz/ply)
- pytest (for running tests)

## Installation and Usage

1. **Create and Activate a Virtual Environment**:
   - Linux: `python -m venv venv` and `source venv/bin/activate`
   - Windows: `python -m venv venv` and `.\venv\Scripts\activate`

2. **Install Dependencies**:
   - Run `pip install -r requirements.txt`

3. **Run the Analyzer**:
   - Execute `python main.py`

4. **Run Unit Tests**:
   - Execute `pytest` in the terminal.
   - All tests should pass, indicating the analyzer's functionality.

### Symbols Table

Stores recognized tokens with types and positions. Example:

```json
{
  "a": {
    "Position": {"line": 3, "pos": 50},
    "Type": "integer"
  },
  ...
}
```

## Test Cases

Test cases focus on identifying lexical, syntax, and semantic errors. Each case targets specific error scenarios, demonstrating the analyzer's robustness in error detection and handling.

## Future Improvements

- **Code Generation**: Implementing the code generation phase to convert intermediate code into executable code, completing the compiler's functionality.
- **Enhanced Error Recovery**: Improving error recovery mechanisms, especially in the syntax analyzer, for better handling of multiple errors in a single run (Panic Mode).

## Conclusion

This project provides insights into compiler construction, especially in analysis phases. Although it doesn't cover code generation, it lays a strong foundation for understanding and developing compilers.
