nm=raw_input()
s=nm.split()
n=long(s[0])
m=long(s[1])
li=[]
sum=0
for i in range(m):
	p=raw_input()
	li.append(map(long, p.split()))
for j in range(m):
	sum+=(li[j][0]-li[j][1]+1)*li[j][2]
print sum/n
