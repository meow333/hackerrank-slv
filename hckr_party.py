r=input()
n=['']*r
for i in range(r):
	n[i]=input()
while(r>0):
	s=n[r-1]/2
	n[r-1]=s*(n[r-1]-s)
	r=r-1
for j in range(len(n)):
	print n[j]
