# *
# 68ms ,81.64%
# Referred @yangshun

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right =0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
    
    
        '''
        # Two pointers
        # Original failed ideas
        l,r = -1, len(nums)
        left, right = 0, 0
        while(l < r):
            if left > right:
                r -= 1
            if right > left:
                l += 1
            else:
                r -= 1
                l += 1
            if l != r:
                left += nums[l]
                right += nums[r]
        if left == right:
            return l
        else:
            return -1
        '''
