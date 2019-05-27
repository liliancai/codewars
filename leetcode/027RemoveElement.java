//0ms,100%
class Solution {
    public int removeElement(int[] nums, int val) {
        int count=0;
        for(int i=0;i<nums.length;i++){
            if(val!=nums[i]){
                nums[count++]=nums[i];
            }
        }
        return count;
    }
}
-------------------another solution--------------------------------
    class Solution {
    public int removeElement(int[] nums, int val) {
        //two pointers!
        int n = nums.length;
        int j = n-1,i = 0;
        while(i<=j){
            if(nums[j]==val){
                j--;
                continue;
            }
            if(nums[i]!=val){
                i++;
                continue;
            }
            nums[i]=nums[j];
            j--;
        }
        return j+1;
    }
}
// above would produce less move but with more compare, in the contrast with below.
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int j = n-1,i = 0; //tail and head
        while(i<=j){
            if(nums[i] == val){     
                nums[i] = nums[j];
                j--;
            }else i++;
        }
        return j+1;
    }
}
