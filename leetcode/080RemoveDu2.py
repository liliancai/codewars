# Index error in comment
# Inspired by @letcodee
# Runtime 54ms, 64%


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        length = len(nums)
        while i < length:
            if nums[i] == nums[i-2]:
                del nums[i]
                length -=1
            else:
                i += 1
        return length
        
        """
        for each in nums:
            if each == nums[i-2]:
                nums.remove(each)
            else:
                i +=1
            '''
        for i in range(len(a)):
            if a[i] != -999:
                result += 1
                nums[i] = a[i]'''
        return len(nums)
        """
