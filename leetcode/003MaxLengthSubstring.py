# Return the length of longest non-repeated substring

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        appearedChar = {}
        max_length = 0
        for i in range(len(s)):
            if s[i] in appearedChar and appearedChar[s[i]] >= start:
                start = appearedChar[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            appearedChar[s[i]] = i
        return max_length

