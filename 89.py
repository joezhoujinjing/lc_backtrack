class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result=['0'*n]
        od=n-1
        direction=-1
        while len(result)<2**n:
        	tmp=result[-1][:od]+str(1-int(result[-1][od]))+result[-1][od+1:]
        	result.append(tmp)
        	od+=direction
       		if od==n-1:
       			direction=-1
       		if od==0:
       			direction=1
       	print result
        return [int(r,2) for r in result]



sl=Solution()
print sl.grayCode(3)