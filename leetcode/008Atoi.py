class Solution:
    """
    strip then pick up list[0]
    64ms 50%
    """
    def myAtoi(self, str: str) -> int:
         
        l=list(str.strip())
        if len(l) == 0:
            return 0
        sign = -1 if l[0] == '-' else 1      
        if l[0] in '+,-':
            # remove l[0]
            del l[0]
        sum ,i = 0,0
        while i<len(l) and l[i].isdigit():
            sum = sum*10 + ord(l[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign*sum, 2**31-1))
