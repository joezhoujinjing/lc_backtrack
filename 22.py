class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res=[]
        
        def bt(l,r,pre):
            if len(pre)>n*2:
                return
            if len(pre)==n*2 and l==r:
                self.res.append(pre)
                return
            if l<r:
                return
            bt(l+1,r,pre+'(')
            bt(l,r+1,pre+')')
        bt(0,0,'')
        return self.res
        
sl=Solution()
print sl.generateParenthesis(3)