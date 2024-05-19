

"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==1:
            return nums[0]


        nByTwo = int(len(nums)/2)
        nums.sort()

        output=0
        count=1
        previous = nums[0]
        for item in nums[1:]:
            if previous==item:
                count+=1
                if count>nByTwo:
                    output = item
                    break
                continue
            else:
                count=1
                previous=item

        return output


    def __main__(self):
      

        nums = [1]
        print(f"nums: {nums}")
        print(self.majorityElement(self, nums))


Solution.__main__(Solution) 
