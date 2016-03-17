class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.cand=range(1,n+1)
        self.res=[]

        def bt(l,idx):
        	if len(l)==k:
        		self.res.append(l)
        		return
        	for i in range(idx,len(self.cand)):
        		bt(l+[self.cand[i]],i+1)
        bt([],0)
        return self.res


sl=Solution()
print sl.combine(4,2)