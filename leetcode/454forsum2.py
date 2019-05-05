class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # a hash table to save the all a+b then how much all -(c+d) in it
        # o(n2),312ms, 67.91%, 34mb
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
    
 ------------------faster--------------------
       
 class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # Runtime: 284 ms, faster than 77.54% of Python3 online submissions for 4Sum II.
        '''
        hashtable = {}
        for a in A:
            for b in B :
                #if a + b in hashtable :
                 #   hashtable[a+b] += 1
                #else :
                 
        
        hashtable[a+b] = 1
        '''
        hashtable = collections.Counter(a+b for a in A for b in B)
        count = 0         
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count
       
------------------faster--------------------
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 272 ms, faster than 82.46%, 34mb
        # gueeśs because of line 17&18
        hashtable = {}
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count
