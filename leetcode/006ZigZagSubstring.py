class Solution(object):
	"""
	Runtime 112ms 41%
	Took 3 hours to code and debug
	Cause the complexity of my index design
	"""
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >len(s):
             return s
        sub=[''] * numRows
        # So hard to decide the last column!
		# Either I make it general or I make it special
		# General is better but how to add condition....
        G = 2*numRows-2
        p = len(s)//G
        if len(s)-p*G >0:
            p+=1
        for i in range(p): 
			 # Deal with the last column
            j = 0
            index = i*G
            while j < numRows:
                sub[j] += s[index+j]
                if index+j == len(s)-1:
                     return ''.join(sub)
                else:
                     j+=1

            j = 1
            while j < numRows-1:
                sub[numRows-j-1] += s[index+numRows+j-1]  
                if index+numRows+j-1 == len(s)-1:
                     print(''.join(sub))
                     return ''.join(sub)
                else:
                     j+=1 

'''
# @pharrellyhy, runtime 64ms, and it's so pretty, hope one day I can code like this!
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

  		return ''.join(L)
'''

if __name__ == "__main__":
	assert Solution.convert("","PAYPALISHIRING",3) == "PAHNAPLSIIGYIR"
	assert Solution.convert("","PAYPALISHIRING",4) == "PINALSIGYAHRPI"
	assert Solution.convert("","PAYPALISHIRING",1) == "PAYPALISHIRING"
