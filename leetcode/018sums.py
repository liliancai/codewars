class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 164ms 64.69%
        # 
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
