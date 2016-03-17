class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        def bt(s,digits):
        	if digits=='':
        		res.append(s)
        		return
        	dig=digits[0]
        	for c in d[dig]:
        		bt(s+c,digits[1:])

        bt('',digits)
        return res

sl=Solution()
print sl.letterCombinations('23')