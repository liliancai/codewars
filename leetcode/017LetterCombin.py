# 36 ms,70.14%
# refered @huxley
# python3 need functools to use reduce

import functools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        return functools.reduce(lambda acc, digit:[x+y for x in acc for y in kvmaps[digit]], digits,[''])
