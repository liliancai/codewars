//Runtime: 1 ms, faster than 85.64% of Java online submissions for Implement strStr().
class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length()==0){
            return 0;
        }
        int lh=haystack.length();
        int ln=needle.length();
        int i;
        for(i=0; i<lh-ln+1;i++){
            int count=0;
            while(haystack.charAt(i+count)==needle.charAt(count)){
                count++;
                if(count==ln){
                    break;
                }
            }
            if(count==ln){
                return i;
            }
        }
        return -1;
    }
}
