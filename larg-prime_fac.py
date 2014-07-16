def pf(n):
    p=n
    a=[]
    while p>1:
        if n%p==0 and pc(p)==1:
            return p
        p=p-1

def pc(n):
    p=2
    f=0
    while p<(n/2)+1:
        if n%p==0:
            return False
        p=p+1
    return True
##    if f==0:
##        return 1
##    else:
##        return 0
##            

t=int(input())
while t>0:
    n=int(input())
    print(pf(n))
    t=t-1
