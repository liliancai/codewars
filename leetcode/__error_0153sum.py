class Solution:
    def threeSum(self, nums):
        # Make a table save the -sum of each two
        # for for and for
        # if found -sum + List[i] = 0 then return the set
        
        table = [[9999]*len(nums)]*len(nums)
        print(table)
        # table = []
        for i in range(len(nums)):
            j = i+1
            while j<len(nums):
                table[i][j] = (nums[i]+nums[j])*-1
                j +=1
            print(i,table[i])
        print(table)
        ss = []     
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for each in nums:
                    if table[i][j] == each:
                        ss.append((nums[i],nums[j],each))
        return ss


if __name__ == "__main__":
	print("amin")
	Solution().threeSum([-1,0,1,2,-1,-4])
