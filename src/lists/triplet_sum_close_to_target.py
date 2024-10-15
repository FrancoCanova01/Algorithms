import math
import unittest

# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as
# close to the target number as possible, return the sum of the triplet. If there are more than one 
# such triplet, return the sum of the triplet with the smallest sum.

# Example 1:
# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: The triplet [-1, 0, 3] has the sum '2' which is closest to the target. There are two triplets 
# with distance '1' from the target: [-1, 0, 3] & [-1, 2, 3]. Between these two triplets, the correct answer 
# will be [-1, 0, 3] as it has a sum '2' which is less than the sum of the other triplet which is '4'. This 
# is because of the following requirement: 'If there are more than one such triplet, return the sum of the 
# triplet with the smallest

# Example 2:
# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

# Example 3:
# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.

# Example 4:
# Input: [0, 0, 1, 1, 2, 6], target=5
# Output: 4
# Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0, 0, 6].
# Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4' which is less than 
# the sum of the other triplet which is '6'. This is because of the following requirement: 'If there are more 
# than one such triplet, return the sum of the triplet with the smallest sum.'

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()

    best_dist = math.inf
    best_sum = math.inf

    for index, i in enumerate(arr):
        # Skip repeated elements
        if index > 0 and arr[index] == arr[index - 1]:
            continue

        left = index + 1
        right = len(arr) - 1

        while left < right:
            current_sum = i + arr[right] + arr[left]
            dist = abs(target_sum - current_sum)

            if dist == 0:
                return current_sum
        
            # Update best_dist and best_sum
            if dist < best_dist or (dist == best_dist and current_sum < best_sum):
                best_dist = dist
                best_sum = current_sum

            if current_sum < target_sum:
                # You need to increase current sum by increasing left pointer
                left += 1
            else:
                # You need to decrease current sum by decreasing right pointer
                right -= 1
            
    return best_sum


class TestTripletSumCloseToTarget(unittest.TestCase):
    def test_1(self):
        output = triplet_sum_close_to_target([0,0,1,1,2,6], 5)
        self.assertEqual(output, 4)

    def test_2(self):
        output = triplet_sum_close_to_target([-1, 0, 2, 3], 3)
        self.assertEqual(output, 2)
    
    def test_3(self):
        output = triplet_sum_close_to_target([-3, -1, 1, 2], 1)
        self.assertEqual(output, 0)
    
    def test_4(self):
        output = triplet_sum_close_to_target([1, 0, 1, 1], 100)
        self.assertEqual(output, 3)

    def test_5(self):
        output = triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5)
        self.assertEqual(output, 4)

if __name__ == '__main__':
    unittest.main()

                
            

            

