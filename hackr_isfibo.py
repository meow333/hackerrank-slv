#isfibo
for i in range(input()):
	a=long(0)
	b=long(1)
	t=long(input())
	while(b<=t):
		c=long(a)
		a=b
		b=c+b
	if a==t:
		print "IsFibo"
	else:
		print "IsNotFibo"
	
