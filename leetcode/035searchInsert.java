//Runtime: 0 ms, faster than 100.00% of Java online submissions for Search Insert Position.
// hmm can go faster?
class Solution {
    public int searchInsert(int[] nums, int target) {
        int i;
        for(i=1;i<nums.length;i++){
            if(target==nums[i]||(target < nums[i]& target> nums[i-1])){
                return i;
            }
        }
        if(target > nums[i-1]){
            return i;
        }
        return 0;
    }
}
