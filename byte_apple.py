fc = open("apple-computers.txt", "r")
ff = open("apple-fruit.txt", "r")
r1=fc.read()
r2=ff.read()
d=unicode(raw_input())
l=0

def chk(text):
    global r1,r2
    flagf=0
    flagc=0
    for i in range(len(text)):
        if text[i] in r2 and len(text[i])>2:
            flagf=flagf+1
        if text[i] in r1 and len(text[i])>2:
            flagc=flagc+1
    #print flagc, flagf
    if flagc>flagf:
        return "computer-company"
    else:
        return "fruit"

for i in xrange(len(d)):
    if d[i]=="\n":
        flagf=0
        flagc=0
        r=i
        text=d[l:r].split()
        l=r
        if len(text)>1:
            print chk(text)
        
    if i==len(d)-1:
        flagf=0
        flagc=0
        text=d[l:].split()
        if len(text)>1:
            print chk(text)
        

