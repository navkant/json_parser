from lexer import lex
from parser import parse


def from_string(string: str):
    tokens = lex(string)
    return parse(tokens)[0]


if __name__ == "__main__":
    example_string = '{"foo": [1, 2, {"bar": 2}]}'
    print(f"example json: '{example_string}'")
    print(from_string(example_string))
