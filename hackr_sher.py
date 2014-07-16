t=input()
while(t!=0):
	p=['']*t
	for i in range(t):
		p[i]=raw_input().split()
		for j in range(len(p[i])):
			p[i][j]=long(p[i][j], base=10)
	for i in range(t):
		c=0
		c=long(c)
		for j in range(p[i][0]):
			if j*(p[i][0]-j) <= p[i][0]*p[i][1]:
				c=c+1
		c=c-1
		print c
	t=input()
