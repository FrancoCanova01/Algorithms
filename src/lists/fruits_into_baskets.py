import unittest

# You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
# You will be given two baskets, and your goal is to pick as many fruits as possible 
# to be placed in the given baskets.

# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

# Each basket can have only one type of fruit. There is no limit to how many fruit a 
# basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, 
# i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

# Example 1:
# Input: arr=['A', 'B', 'C', 'A', 'C']  
# Output: 3  
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:
# Input: arr = ['A', 'B', 'C', 'B', 'B', 'C']  
# Output: 5  
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def longest_substring_with_k_distinct_characters(str1, k): # O(n)

    window_start = 0
    window_end = 0
    longest_sbstr = 0
    char_k = {}

    while window_end <= len(str1) - 1:
        if str1[window_end] in char_k:
            char_k[str1[window_end]] += 1
        else:
            char_k[str1[window_end]] = 1

        if len(char_k.keys()) <= k:
            current_length = window_end - window_start + 1
            longest_sbstr = current_length if current_length >= longest_sbstr else longest_sbstr
        elif len(char_k.keys()) > k:
            char_k[str1[window_start]] -= 1
            char_k[str1[window_end]] -= 1
            if char_k[str1[window_start]] == 0:
                del char_k[str1[window_start]]
            
            window_start += 1
            continue

        window_end += 1

    return longest_sbstr


def fruits_into_baskets(arr):
    # The problem can be reduced to longest_substring_with_k_distinct_characters_v2
    k = 2 # baskets
    return longest_substring_with_k_distinct_characters("".join(arr), k)


class Test(unittest.TestCase):
    def test_1(self):
        output = fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
        expected = 3
        self.assertEqual(output, expected)

    def test_2(self):
        output = fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])
        expected = 5
        self.assertEqual(output, expected)

    def test_3(self):
        output = fruits_into_baskets(['A', 'A', 'A', 'A'])
        expected = 4
        self.assertEqual(output, expected)

unittest.main()