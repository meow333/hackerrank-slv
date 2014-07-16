n=raw_input();
n1=""
n2=""
for i in range(len(n)):
	if n[i] == " ":
		for j in range(i):
			n1=n1+n[j]
		n1=int(n1)
		print n1, type(n1)
		for k in range(i+1,len(n)):
			n2=n2+n[k]
		n2=int(n2)
		print n2, type(n2)
