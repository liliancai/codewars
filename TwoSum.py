class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,each_i in enumerate(nums): 
            if target >= each_i:
                for j, each_j in enumerate(nums):
                    if target >= each_j:
                        (each_i + each_j) == target
                        return [i, j]

def test_result(UnitTest):
	
if __name__ == "__main__":
	test_result()


'''
# O(n) from @jiaming from @jiaming2
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
'''
