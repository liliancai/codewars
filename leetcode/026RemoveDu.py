class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = sorted(list(set(nums)))
        for i in range(len(new)):
            nums[i] = new[i]
        return len(new)
-------Java-----------------
// Runtime: 1 ms, faster than 99.88% of Java
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for(int n:nums){
            if( i==0 || n > nums[i-1]){
                nums[i++] = n;
            }
        }
        return i;
    }
}
