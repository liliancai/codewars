
class Solution:
    def reverse(self, x: int) -> int:
        sign = (x>0)-(x<0)
        #r = int(`sign*x`[::-1]) 
        r = int(str(sign*x)[::-1])
        return r*sign*(r<2**31)
