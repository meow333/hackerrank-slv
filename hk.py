####def matrix_circles(a):
####    n=len(a) #ending row index
####    m=len(a[0]) #ending column index
####    k=0 #starting row index
####    l=0 #starting column index
####    while k<m and l<n:
####        for i in range(1,n):
####            print(a[k][i])
####        k=k+1
####        for j in range(k,m):
####            print(a[i][n-1])
####        n=n-1
####        if k<m :
####            for k in reversed(range(1,n-1)):
####                print(a[m-1][i])
####            m=m-1
####        if l<n:
####            for i in reversed(range(k,m-1)):
####                print(a[i][l])
####            l=l+1
####
####    # Write your code here
####
####    # To print results to the standard output you can use print
####    # Example:
####    # print "Hello world!"
####p=input('matrix:')
####import ast
####t=ast.literal_eval(p)
####matrix_circles(t)
##### Do NOT call the matrix_circles function in the code
##### you write. The system will call it automatically.
##ar = [
## [ 0,  1,  2,  3, 4],
## [15, 16, 17, 18, 5],
## [14, 23, 24, 19, 6],
## [13, 22, 21, 20, 7],
## [12, 11, 10, 9, 8]]
##
##def print_spiral(ar):
##    """
##    assuming a rect array
##    """
##    array=[]
##    rows, cols = len(ar), len(ar[0])
##    r, c = 0, -1 # start here
##    nextturn = stepsx = cols # move so many steps
##    stepsy = rows-1
##    inc_c, inc_r = 1, 0 # at each step move this much
##    turns = 0 # how many times our snake had turned
##    for i in range(rows*cols):
##        c += inc_c
##        r += inc_r 
##
##        array.append(ar[r][c])
##
##        if i == nextturn-1:
##            turns += 1
##            # at each turn reduce how many steps we go next
##            if turns%2==0:
##                nextturn += stepsx
##                stepsy -= 1
##            else:
##                nextturn += stepsy
##                stepsx -= 1
##            # change directions
##            inc_c, inc_r = -inc_r, inc_c
##    return tuple(array)
##p=input()
##import ast
##t=ast.literal_eval(p)
##print(print_spiral(t))
def checkPassword(password):
    import re
    pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[+$#\/).(?!\\d{3}).*$"
    result = re.findall(pattern,password)
    if result:
        return "true"
    else:
        return "false"
    # Write your code here

    # To print results to the standard output you can use print
    # Example:
    # print "Hello world!"
checkPassword(input())
