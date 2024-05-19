
"""

100300. Sum of Digit Differences of All Pairs
User Accepted:6318
User Tried:9335
Total Accepted:6660
Total Submissions:16998
Difficulty:Medium
You are given an array nums consisting of positive integers where all integers have the same number of digits.

The digit difference between two integers is the count of different digits that are in the same position in the two integers.

Return the sum of the digit differences between all pairs of integers in nums.

 

Example 1:

Input: nums = [13,23,12]

Output: 4

Explanation:
We have the following:
- The digit difference between 13 and 23 is 1.
- The digit difference between 13 and 12 is 1.
- The digit difference between 23 and 12 is 2.
So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.

Example 2:

Input: nums = [10,10,10,10]

Output: 0

Explanation:
All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.

 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] < 109
All integers in nums have the same number of digits.

"""


class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = 0
        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)):
                i_value = nums[i]
                i_total = self.getSum(i_value)
                j_value = nums[j]
                j_total = self.getSum(j_value)
                total += i_total-j_total
        return total
  

    def getSum(value): 
        sum = 0
        while (value!= 0): 
            sum = sum + int(value%10)
            value = value//10
        return sum
    
solution = Solution
nums = [13,23,12]
sum = solution.getSum(nums)
print(f'Sum: {sum}')
