# Given a sorted array, remove the duplicates in place such that 
# each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, 
# you must do this in place with constant memory.
# 
# For example, Given input array nums = [1,1,2],
# 
# Your function should return length = 2, 
# with the first two elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the new length.

# Use Two Pointers
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        # Learn how to write NEAT code !
        # By merging, rearranging and cleaning messy logic sentences.
        for i in range(len(nums)):
            if not i or nums[i] != nums[i - 1]:
                nums[cnt] = nums[i]
                cnt += 1
                
        return cnt
    
nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))