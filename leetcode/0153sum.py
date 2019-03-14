# Around 1000ms, 60%
# Once add if nums[i] > 0: return rs
# Become 872ms, 75%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Should think more solution
        # table is the least way to do that
        # sort nums
        # from the left one by one check the rest if have a pair to match it
        # and skip the same , like a+b=c is there is 2a would be 2 same solution
        # I also want to try if nums[i]>0 there is not much liking to find solution anymore
        # cause positive + positve also positive unless 0+0+0
        
        rs = []
        nums.sort()
        print(nums)
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = N-1
            target = nums[i]*-1
            while l<r:
                if nums[l]+nums[r] == target: #bingo
                    rs.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] < target:
                    l+=1 
                else:
                    r-=1 
          #  if nums[i]>0:
          #      return rs
        return rs
        
    
