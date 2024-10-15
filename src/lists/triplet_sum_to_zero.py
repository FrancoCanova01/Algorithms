
import unittest

# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# Explanation: There are four unique triplets whose sum is equal to zero. smallest sum.'

# Example 2:
# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

def triplet_search_for_zero(arr): # Complexity: 
    triplets = []
    arr.sort() # log n * n

    for i in range(len(arr)):
        # For each element, check if it's the same as the previous one to avoid duplicates.
        if i > 0 and arr[i] == arr[i-1]:
            continue

        p1 = i + 1
        p2 = len(arr) - 1

        while p1 < p2:
            sum = arr[p1] + arr[p2]

            if sum + arr[i] == 0:
                # Create triplet and append to triplets array
                triplets.append([arr[p1], arr[p2], arr[i]])

                # Move both pointers
                p1 += 1
                p2 -= 1

                # Move pointers if same value to avoid duplicates.
                while p1 < p2 and arr[p1] == arr[p1 - 1]:
                    p1 += 1  # skip same element to avoid duplicate triplets
                while p1 < p2 and arr[p2] == arr[p2 + 1]:
                    p2 -= 1  # skip same element to avoid duplicate triplets
            else:
                if sum + arr[i] < 0:
                    # increase sum by increasing the left pointer
                    p1 += 1
                else:
                    # decrease sum by decreasing the left pointer
                    p2 -= 1
    
    return triplets

class TestTripletSearchForZero(unittest.TestCase):
    def test_1(self):
        output = triplet_search_for_zero([-5, 2, -1, -2, 3])
        self.assertEqual(len(output), 2)
        for i in output:
            self.assertEqual(sum(i), 0)
            
    def test_2(self):
        output = triplet_search_for_zero([-3,0,1,2,-1,1,-2])
        self.assertEqual(len(output), 4)
        for i in output:
            self.assertEqual(sum(i), 0)
    
    def test_empty(self):
        output = triplet_search_for_zero([])
        self.assertEqual(len(output), 0)
        for i in output:
            self.assertEqual(sum(i), 0)
    
    def test_one_answer(self):
        output = triplet_search_for_zero([-3,2,1])
        self.assertEqual(len(output), 1)
        for i in output:
            self.assertEqual(sum(i), 0)
    
    def test_empty_answer(self):
        output = triplet_search_for_zero([-3,2,2])
        self.assertEqual(len(output), 0)
        for i in output:
            self.assertEqual(sum(i), 0)
    
    def test_3(self):
        output = triplet_search_for_zero([-1,0,1,2,-1,-4])
        self.assertEqual(len(output), 2)
        for i in output:
            self.assertEqual(sum(i), 0)


if __name__ == '__main__':
    unittest.main()