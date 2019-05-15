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
--------------------------Java------------------------
//Runtime: 2 ms, faster than 99.41% of Java online submissions for Two Sum.
// Compared to around 44ms Python...the speed is amazing!
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> Bucket = new HashMap <Integer, Integer>();
        int len = nums.length;
        for(int i=0; i<len; i++){
            if(Bucket.containsKey(nums[i])){
                int left=Bucket.get(nums[i]);
                return new int[]{left,i};
            }else{
                Bucket.put(target-nums[i],i);
            }
        }
        return new int[2];
    }
}
