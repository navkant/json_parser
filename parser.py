from constants import (
    JSON_COMMA,
    JSON_QUOTE,
    JSON_COLON,
    JSON_LEFTBRACE,
    JSON_RIGHTBRACE,
    JSON_LEFTBRACKET,
    JSON_RIGHTBRACKET,
)

from typing import List, Dict


def parse_array(tokens: List[str]) -> (List[str], List[str]):
    json_array = []

    token = tokens[0]

    if token == JSON_RIGHTBRACKET:
        return json_array, tokens[1:]

    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        token = tokens[0]
        if token == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]
        elif token != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]

    raise Exception('Expected end of array bracket')


def parse_object(tokens: List[str]) -> (Dict, List[str]):
    json_object = {}

    token = tokens[0]
    if token == JSON_RIGHTBRACE:
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception(f'Expected string key, got: {json_key}')

        if tokens[0] != JSON_COLON:
            raise Exception(f'Expected colon after key in object, got: {token}')

        json_value, tokens = parse(tokens[1:])
        json_object[json_key] = json_value

        token = tokens[0]
        if token == JSON_RIGHTBRACE:
            return json_object, tokens[1:]
        elif token != JSON_COMMA:
            raise Exception(f'Expected comma after a pair in object, got {token}')

        tokens = token[1:]

    raise Exception(f'Expected end-of-object brace')


def parse(tokens: List[str]):
    token = tokens[0]

    if token == JSON_LEFTBRACKET:
        return parse_array(tokens[1:])
    elif token == JSON_LEFTBRACE:
        return parse_object(tokens[1:])
    else:
        return token, tokens[1:]