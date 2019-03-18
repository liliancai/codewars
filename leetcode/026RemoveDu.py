class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = sorted(list(set(nums)))
        for i in range(len(new)):
            nums[i] = new[i]
        return len(new)
