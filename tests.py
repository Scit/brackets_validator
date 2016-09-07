import unittest
from brackets_validator import is_valid_brackets


class TestBracketsValidator(unittest.TestCase):
    def test_empty_valid(self):
        result = is_valid_brackets('')
        self.assertTrue(result)

    def test_valid_braces(self):
        result = is_valid_brackets('{}')
        self.assertTrue(result)

    def test_valid_square(self):
        result = is_valid_brackets('[]')
        self.assertTrue(result)

    def test_valid_parentheses(self):
        result = is_valid_brackets('()')
        self.assertTrue(result)

    def test_valid_combo(self):
        result = is_valid_brackets('[{}({})]')
        self.assertTrue(result)

    def test_invalid_unclosed(self):
        result = is_valid_brackets('[[')
        self.assertFalse(result)

    def test_invalid_unmatched(self):
        result = is_valid_brackets('[[})')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
