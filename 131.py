class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.s=s
        self.res=[]
        def palin(s):
        	if s=='':
        		return False
        	if len(s)==1:
        		return True
        	i=0
        	j=len(s)-1
        	while i<j:
        		if s[i]!=s[j]:
        			return False
        		i+=1
        		j-=1
        	return True

        def bt(idx,tmp):
        	if idx>len(s):
        		return
        	if idx==len(s):
        		self.res.append(tmp)
        		tmp=[]
        		return
        	for i in range(idx+1,len(s)+1):
        		if palin(s[idx:i]):
        			bt(i,tmp+[s[idx:i]])
        bt(0,[])
        return self.res

sl=Solution()
print sl.partition('aab')