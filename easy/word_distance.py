import unittest
import math

# Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

# Example 1:
# Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
# Output: 5
# Explanation: The distance between "fox" and "dog" is 5 words.

# Example 2:
# Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
# Output: 1
# Explanation: The shortest distance between "a" and "b" is 1 word. Please note that "a" appeared twice.

# Example 3:
# Input: words = ["a", "b", "c", "d", "e"], word1 = "a", word2 = "e"
# Output: 4
# Explanation: The distance between "a" and "e" is 4 words.

def shortestDistance(words, word1, word2):
    shortestDistance = len(words) # Initialize the shortest distance with the length of the words list
    position1, position2 = -1, -1 # Initialize the positions of word1 and word2 with -1
    for i, word in enumerate(words):
        if word == word1: # If the current word is word1, update the position1
            position1 = i
        elif word == word2: # If the current word is word2, update the position2
            position2 = i

        # If both the positions are updated, update the shortest distance
        if position1 != -1 and position2 != -1:
            shortestDistance = min(shortestDistance, abs(position1 - position2))

    return shortestDistance

class TestShortestDistance(unittest.TestCase):
    def test_words_exist(self):
        self.assertEqual(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"), 3)
        self.assertEqual(shortestDistance(["a", "b", "c", "d", "e"], "a", "e"), 4)

    def test_words_close_together(self):
        self.assertEqual(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes"), 1)
        self.assertEqual(shortestDistance(["a", "b", "c", "d", "e"], "a", "b"), 1)

    def test_words_far_apart(self):
        self.assertEqual(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "practice", "makes"), 1)
        self.assertEqual(shortestDistance(["a", "b", "c", "d", "e"], "a", "e"), 4)

if __name__ == '__main__':
    unittest.main()