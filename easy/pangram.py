import unittest
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false otherwise.

# Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

# Example 1:
# Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
# Output: true
# Explanation: The sentence contains at least one occurrence of every letter of the English alphabet either in lower or upper case.

# Example 2:
# Input: sentence = "This is not a pangram"
# Output: false
# Explanation: The sentence doesn't contain at least one occurrence of every letter of the English alphabet.

def checkIfPangram(sentence):
    # TODO: Write your code here
    s = set()
    for x in sentence:
        if x.isalpha():
            s.add(x.lower())

    if len(s) == 26:
        return True

    return False

class TestCheckIfPangram(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(checkIfPangram(""))

    def test_single_letter(self):
        self.assertFalse(checkIfPangram("a"))

    def test_missing_letters(self):
        self.assertFalse(checkIfPangram("The quick brown fox jumps over the lazy do"))

    def test_valid_pangram(self):
        self.assertTrue(checkIfPangram("The quick brown fox jumps over the lazy dog"))

    def test_valid_pangram_with_uppercase(self):
        self.assertTrue(checkIfPangram("The Quick Brown Fox Jumps Over The Lazy Dog"))

    def test_non_alpha_characters(self):
        self.assertTrue(checkIfPangram("The quick brown fox jumps over the lazy dog! 123"))

    def test_pangram_with_repeated_letters(self):
        self.assertTrue(checkIfPangram("Pack my box with five dozen liquor jugs"))

    def test_alphabet_pangram(self):
        self.assertTrue(checkIfPangram("abcdefghijklmnopqrstuvwxyz"))

    def test_alphabet_pangram_uppercase(self):
        self.assertTrue(checkIfPangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

if __name__ == '__main__':
    unittest.main()