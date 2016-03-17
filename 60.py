import math
import copy
class Solution(object):
	def getPermutation(self, n, k):
	    """
	    :type n: int
	    :type k: int
	    :rtype: str
	    """
	    self.count=0
	    self.res=''
	    def bt(cand,l):
	    	if len(l)==n:
	    		self.count+=1
	    		print l
	    		if self.count==k:
	        		self.res+=l
	        		return 
	    		return 
	    	for c in cand:
	    		if self.count>k-1:
	    			break
	    		bt(cand[:cand.index(c)]+cand[cand.index(c)+1:],l+str(c))
	    bt(range(1,n+1),'')
	    return self.res

	def getPermutation2(self,n,k):
		nums=map(str,range(1,10))
		k-=1
		factorial=1
		for i in range(1,n):
			factorial*=i
		print factorial
		res=[]
		for i in reversed(range(n)):
			res.append(nums[k/factorial])
			nums.remove(nums[k/factorial])
			print res,nums,k
			if i!=0:
				k%=factorial
				factorial/=i
		return ''.join(res)
sl=Solution()
print sl.getPermutation(4,10)
print 
print sl.getPermutation2(4,6)