'''
def longestPalindrome(self, s: str) -> str:
	"""
	v1
	O(n^2), 10%
	"""
        max_sub=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                # print(len(s)-i)
                sub = s[i:j+1]
                # print(sub)
                if sub == sub[::-1] and len(sub)>=len(max_sub):
                    max_sub = sub
        return max_sub
'''

def longestPalindrome(self, s: str) ->str:
	"""
	search panlindrome from longest substr
	"""
	for i in range(len(s)):
		for j in range(i, len(s), -1):
			sub = s[i:j+1]
			if sub == sub[::-1]:
				return sub
"""
# @DIZ
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
"""
if __name__ == "__main__":
	assert longestPalindrome("","abba") == "abba"
