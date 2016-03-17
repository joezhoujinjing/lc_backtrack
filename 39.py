class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]
        candidates.sort()
        def bt(l,target):
            if target==0:
                l.sort()
                self.res.append(l)
            for c in candidates:
                if c<=target:
                    bt([c]+l,target-c)
        bt([],target)
        return self.res

    def combinationSum2(self, candidates, target):
        self.res=[]
        self.cl=len(candidates)
        self.cand=candidates.sort()
        def bt(l,idx,target):
            if target<0:
                return
            if target==0:
                self.res.append(l)
            else:
                for i in range(idx,self.cl):
                    bt(l+[self.cand[i]],i,target-self.cand[i])
        bt([],0,target)
        return self.res
sl=Solution()
print sl.combinationSum2([8,7,4,3],11)