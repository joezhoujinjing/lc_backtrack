class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        
        def bt(num,l):
            if num==[]:
                res.append(l)
            for i in xrange(len(num)):
                if i !=0 and num[i] in num[:i]:
                    continue
                bt(num[:i]+num[i+1:],l+[num[i]])
        bt(nums,[])
        return res
sl=Solution()
print sl.permuteUnique([1,1,2])