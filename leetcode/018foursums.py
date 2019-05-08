class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Runtime: 156 ms, faster than 66.85% of Python3 online submissions for 4Sum.
        # Runtime: 132 ms, faster than 75.41% of Python3 online submissions for 4Sum.
        # Runtime: 140 ms, faster than 72.42% of Python3 online submissions for 4Sum.
        # save each two sum in a dict
        # then check if target-(a,b) in dict or not
        # so we need a result set, a twosum dict[twosum]:(a,b)
        
        
        twosums=collections.defaultdict(list)
        result=set()
        for a in range(len(nums)):
            for b in range(a,len(nums)):
                twosums[nums[a]+nums[b]].append((a,b))
                
        for p1 in twosums:
            if target-p1 not in twosums:
                continue
            # if ab!=cd
            for a,b in twosums[p1]:
                for c,d in twosums[target-p1]:
                    result.add(tuple(sorted({a,b,c,d})))
                    
        
        # have to remove all the duplicated case
        # lambda only return non repeated abcd
        return list(
                    set(
                        tuple(sorted([nums[a],nums[b],nums[c],nums[d]])) 
                        for a,b,c,d in filter(lambda p:len(p)==4,result)
                 ))

    
    
    ------------------------------v2------------------------------------
    class Solution:
    def uniq(self,lst):
        last = object()
        for item in lst:
            if item == last:
                continue
            yield item
            last = item
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Runtime: 144 ms, faster than 70.59% of Python3 online submissions for 4Sum.
        # Runtime: 132 ms, faster than 75.41% of Python3 online submissions for 4Sum.
        # Runtime: 140 ms, faster than 72.42% of Python3 online submissions for 4Sum. 
        
        twosums=collections.defaultdict(list)
        result=set()
        for a in range(len(nums)):
            for b in range(a,len(nums)):
                twosums[nums[a]+nums[b]].append((a,b))
                
        for p1 in twosums:
            if target-p1 not in twosums:
                continue
            # if ab!=cd
            for a,b in twosums[p1]:
                for c,d in twosums[target-p1]:
                    result.add(tuple(sorted({a,b,c,d})))
                    
        
        # have to remove all the duplicated case
        # lambda only return non repeated abcd
        results = list(sorted([nums[a],nums[b],nums[c],nums[d]]) for a,b,c,d in filter(lambda p:len(p)==4,result))
        return list(self.uniq(sorted(results)))
