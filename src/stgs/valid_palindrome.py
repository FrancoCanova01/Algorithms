import unittest

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: sentence = "A man, a plan, a canal, Panama!"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: sentence = "Was it a car or a cat I saw?"
# Output: true
# Explanation: Explanation: "wasitacaroracatisaw" is a palindrome.

def isPalindrome(s: str) -> bool:
    s = [*s]
    clean_s = [c.lower() for c in s if c.isalnum()]
    s1 = "".join(clean_s)
    clean_s.reverse() 
    return s1 == "".join(clean_s)


class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))

    def test_single_character(self):
        self.assertTrue(isPalindrome("a"))
        self.assertTrue(isPalindrome("Z"))

    def test_palindrome_alphanumeric(self):
        self.assertTrue(isPalindrome("level"))
        self.assertTrue(isPalindrome("racecar"))

    def test_non_palindrome_alphanumeric(self):
        self.assertFalse(isPalindrome("hello"))
        self.assertFalse(isPalindrome("world"))

    def test_palindrome_mixed_characters(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(isPalindrome("Able was I, ere I saw Elba!"))

    def test_non_palindrome_mixed_characters(self):
        self.assertFalse(isPalindrome("not a palindrome!"))
        self.assertFalse(isPalindrome("123abc321"))

if __name__ == '__main__':
    unittest.main()