import copy
class Solution(object):
	'''
    def exist(self, board, word):
        self.res=False
        def bt(maps,w,p,path):
        	print p
        	if len(w)==1:
        		self.res=True
        		return
        	(r,c)=p
	        if r<len(maps)-1 and maps[r+1][c]==w[1] and (r+1,c) not in path:
	        	bt(maps,w[1:],(r+1,c),path+[(r+1,c)])
	        if r>0 and maps[r-1][c]==w[1] and (r-1,c) not in path:
	        	bt(maps,w[1:],(r-1,c),path+[(r-1,c)])
	        if c<len(maps[0])-1 and maps[r][c+1]==w[1] and (r,c+1) not in path:
	        	bt(maps,w[1:],(r,c+1),path+[(r,c+1)])
	        if c>0 and maps[r][c-1]==w[1] and (r,c-1) not in path:
	        	bt(maps,w[1:],(r,c-1),path+[(r,c-1)])

		
        for r,row in enumerate(board):
	    		for c,col in enumerate(row):
	    			if self.res==True:
	    				return self.res
	    			if col == word[0]:
	    				bt(board,word,(r,c),[])
        return self.res
    '''
	def exist2(self, board, word):
		if not board:
		    return False
		for i in xrange(len(board)):
		    for j in xrange(len(board[0])):
		        if self.dfs(board, i, j, word):
		            return True
		return False

	# check whether can find word, start at (i,j) position    
	def dfs(self, board, i, j, word):
	    print word
	    if len(word) == 0: # all the characters are checked
	    	return True
	    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
	        return False
	    tmp = board[i][j]  # first character is found, check the remaining part
	    board[i][j] = "#"  # avoid visit agian 
	    # check whether can find "word" along one direction
	    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
	    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
	    board[i][j] = tmp
	    return res


       
board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
#board=[['C','A','A'],['A','A','A'],['B','C','D']]
b=["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
board=[]
for _ in b:
	board.append(list(_))
'''
"ABCE",
"SFCS",
"ADEE"
'''
word="ABCCED"
#word='AAB'
word="baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
sl=Solution()
print sl.exist2(board,word)







