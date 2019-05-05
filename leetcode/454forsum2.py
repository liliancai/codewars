class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # a hash table to save the all a+b then how much all -(c+d) in it
        # o(n2),312ms, 67.91%
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
        
        
------------------faster--------------------
