import unittest
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s= "hello"
# Output: "holle"

# Example 2:
# Input: s= "AEIOU"
# Output: "UOIEA"

# Example 3:
# Input: s= "DesignGUrus"
# Output: "DusUgnGires"

def reverseVowels(s: str) -> str:
    first = 0
    last = len(s) - 1
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    s = [*s]
    while first < last:
        if s[first] not in vowels:
            first += 1
        if s[last] not in vowels:
            last -= 1
        if (s[first] in vowels) and (s[last] in vowels):
            s[last], s[first] = s[first], s[last]
            first += 1
            last -= 1

    return "".join(s)


class TestReverseVowls(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverseVowels(""), "")

    def test_single_character(self):
        self.assertEqual(reverseVowels("a"), "a")
        self.assertEqual(reverseVowels("b"), "b")

    def test_no_vowels(self):
        self.assertEqual(reverseVowels("bcdfg"), "bcdfg")

    def test_only_vowels(self):
        self.assertEqual(reverseVowels("aeiou"), "uoiea")
        self.assertEqual(reverseVowels("AEIOU"), "UOIEA")

    def test_mixed_characters(self):
        self.assertEqual(reverseVowels("hello"), "holle")
        self.assertEqual(reverseVowels("leetcode"), "leotcede")
        self.assertEqual(reverseVowels("aA"), "Aa")

    def test_mixed_case(self):
        self.assertEqual(reverseVowels("HeLLo"), "HoLLe")
        self.assertEqual(reverseVowels("LeEtCoDe"), "LeotCEDe")

    def test_vowels_at_ends(self):
        self.assertEqual(reverseVowels("abecidofu"), "ubocidefa")

if __name__ == '__main__':
    unittest.main()

