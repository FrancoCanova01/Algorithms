import unittest

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "listen", t = "silent"
# Output: true

#Example 2:
# Input: s = "rat", t = "car"
#Output: false

# Example 3:
# Input: s = "hello", t = "world"
# Output: false

def isAnagram(s, t):
    # TODO: Write your code here
    # Traverse first string and count occurences of letters
    occurences = {}
    s = [*s]
    for letter in s: #O(n) where n = len(s)
        if letter in occurences.keys():
            occurences[letter] += 1
        else:
            occurences[letter] = 1

    # Substract occurrences of second string
    t = [*t]
    for letter in t: #O(m) where m = len(t)
        if letter in occurences.keys():
            occurences[letter] -= 1
        else:
            # If letter is found in t that is not in s then 
            # it is not a valid anagram
            return False

    return sum(occurences.values()) == 0

class TestIsAnagram(unittest.TestCase):
    def test_empty_strings(self):
        self.assertTrue(isAnagram("", ""))
        
    def test_single_characters(self):
        self.assertTrue(isAnagram("a", "a"))
        self.assertFalse(isAnagram("a", "b"))
        
    def test_valid_anagrams(self):
        self.assertTrue(isAnagram("listen", "silent"))
        self.assertTrue(isAnagram("debit card", "bad credit"))
        
    def test_invalid_anagrams(self):
        self.assertFalse(isAnagram("hello", "world"))
        self.assertFalse(isAnagram("abc", "abcd"))
        
    def test_case_sensitive_anagrams(self):
        self.assertFalse(isAnagram("Listen", "silent"))
        self.assertTrue(isAnagram("Listen", "siLent"))

    def test_special_characters(self):
        self.assertTrue(isAnagram("an-agr-am", "--nagaram"))
        self.assertTrue(isAnagram("anagram-", "na-garam"))

if __name__ == '__main__':
    unittest.main()