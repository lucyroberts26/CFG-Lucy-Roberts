import unittest
from unittest.mock import patch

def isogram():
    i = input("Enter a word to check if it is an isogram: ")
    i = i.lower()
    letters = set()

    for letter in i:
        if letter.isalpha():
            if letter in letters:
                return False
            letters.add(letter)

    return True
# The patch item allows us to create fake values for the input function to complete testing without having to manually test each word
class TestIsogram(unittest.TestCase):
    @patch("builtins.input", return_value="flower")
    def test_is_isogram_true(self, mock_input):
        self.assertTrue(isogram())
    # This test case checks that the function has correctly identified the isogram and flower is an isogram so it should return true

    @patch("builtins.input", return_value="burrow")
    def test_is_isogram_false(self, mock_input):
        self.assertFalse(isogram())
    # This test checks that the function has identified a word as not an isogram, in this case that is burrow so it should be false.

    @patch("builtins.input", return_value="burRow")
    def test_is_isogram_case_insensitive(self, mock_input):
        self.assertTrue(isogram())
    # This test checks if the function is case sensitive ie. showing that there are no repeatign letters within the same case

    @patch("builtins.input", return_value="123flower?")
    def test_is_isogram_non_alpha(self, mock_input):
        self.assertTrue(isogram())
    # This test checks that the function only takes in letter characters and ignores numbers or characters like ?

if __name__ == "__main__":
    unittest.main()
