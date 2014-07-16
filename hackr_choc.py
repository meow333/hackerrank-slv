num=input()
p=['']*num
for i in range(num):
	p[i]=raw_input().split()
	for j in range(len(p[i])):
		p[i][j]=int(p[i][j])
for i in range(num):
	n=p[i][0]
	c=p[i][1]
	m=p[i][2]
	t=n/c
	w=t
	while w/m:
		c1=w/m
		w=w%m+c1
		t=t+c1
	print t
