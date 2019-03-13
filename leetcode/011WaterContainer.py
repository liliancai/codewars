# Two points method
# Cause it depends on height*width so the farest two lines are best pair
# Hiw to have higher height to get more volume for inner lines
#73ms 42%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j=0,len(height)-1
        water=0
        while (i < j):
            water=max(water,(j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
               i+=1
            else:
               j-=1
    
        return water#
'''
# 100ms 17%
# Trying to improve runtime but got worse--!
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j=0,len(height)-1
        water=0
        while (i < j):
            water=max(water,(j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                if height[i]<height[i+1]:i+=1
                else:i+=2
            else:
                if height[j-1]>height[j]:j-=1
                else:j-=2
    
        return water
 '''
