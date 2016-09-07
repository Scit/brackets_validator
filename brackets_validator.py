#!/usr/bin/python
import sys


def is_valid_brackets(string):
    bracket_stack = []
    bracket_pairs = {'}': '{', ']': '[', ')': '('}
    left_brackets = bracket_pairs.values()

    for bracket in string:
        if bracket in left_brackets:
            bracket_stack.append(bracket)
        elif bracket in bracket_pairs:
            if not bracket_stack or bracket_pairs[bracket] != bracket_stack.pop():
                return False

    return not bracket_stack


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        print is_valid_brackets(args[1])
