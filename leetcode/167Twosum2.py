# Sorted so can use two pointer
# 44ms 50% Python3
# Inspired by 015 3sum & 010 water container
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N=len(nums)
        l,r=0,N-1
        while (l<r):
            if nums[l]+nums[r] == target:
                return l,r
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                r-=1
