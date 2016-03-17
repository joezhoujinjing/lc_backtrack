class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.cand=range(1,10)
        self.res=[]

        def bt(l,target,used,idx):
        	if target==0 and len(l)==k:
        		self.res.append(l)
        		return
        	for i in range(idx,9):
        		if self.cand[i] in used:
        			continue
        		if self.cand[i]>target:
        			break
        		if len(l)==k:
        			break
        		bt(l+[self.cand[i]],target-self.cand[i],used+[self.cand[i]],i+1)
        bt([],n,[],0)
        return self.res

sl=Solution()
print sl.combinationSum3(3,9)