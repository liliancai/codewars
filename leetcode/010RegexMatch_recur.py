# Second try
# Referred the solution of OJ
# 1556ms, 12%, try DP next time!
class Solution:
    def isMatch(self, s: str, p:str) -> bool:
        if not p:return not s
        first_mark = bool(s) and p[0] in {s[0],'.'}
        if len(p)>=2 and p[1] == "*":
            # If p[0] not equal to s[0] but rest after * equal,
            # Or p[0] equal s[0] just move s to next index and remain p
            return self.isMatch(s,p[2:]) or first_mark and self.isMatch(s[1:],p)
        else:
            # If there is not * just make sure the rest matchs too.
            return first_mark and self.isMatch(s[1:],p[1:])
