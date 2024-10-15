import unittest

# Given a string, find the length of the longest substring in it with no more 
# than K distinct characters.

# You can assume that K is less than or equal to the length of the given string.

# Example 1:
# Input: String="araaci", K=2  
# Output: 4  
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:
# Input: String="araaci", K=1  
# Output: 2  
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:
# Input: String="cbbebi", K=3  
# Output: 5  
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_substring_with_k_distinct_characters(str1, k): # O(n)
    
    if k > len(str1):
        return len(str1)

    window_start = 0
    window_end = 0
    longest_sbstr = 0
    char_k = {}

    while window_end <= len(str1) - 1:
        if str1[window_end] in char_k:
            char_k[str1[window_end]] += 1
        else:
            char_k[str1[window_end]] = 1

        if len(char_k.keys()) == k:
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


class Test(unittest.TestCase):
    def test_1(self):
        output = longest_substring_with_k_distinct_characters("araaci", 2)
        expected = 4
        self.assertEqual(output, expected)
    
    def test_2(self):
        output = longest_substring_with_k_distinct_characters("araaci", 1)
        expected = 2
        self.assertEqual(output, expected)
    
    def test_3(self):
        output = longest_substring_with_k_distinct_characters("cbbebi", 3)
        expected = 5
        self.assertEqual(output, expected)

    def test_4(self):
        output = longest_substring_with_k_distinct_characters("aabacbebebe", 3)
        expected = 7
        self.assertEqual(output, expected)

unittest.main()
