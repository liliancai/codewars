"""280ms 40%"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        rev,tmp =0,x
        s=x
        while (tmp>0):
               rev=rev*10+tmp%10
               tmp=tmp//10
     
        if rev == x:
            return True
        else: 
            return False
        
