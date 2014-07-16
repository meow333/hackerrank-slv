def fib(n):
    a, b = 0, 1
    p=[]
    while b < n+1:
        a, b = b, a + b
        if a%2 ==0:
            p.append(a)
    return p

t=int(input())
while t>0:
    n=int(input())
    print(sum(fib(n)))
    t=t-1

