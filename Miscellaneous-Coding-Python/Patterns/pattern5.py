'''
Pattern
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''

def pattern5(n):
    for i in range(1, 2*n):
        if i <=n:
            print("*"*i,end="")
        else:
            print("*"*((2*n)-i),end="")
        print()

n = int(input().strip())
pattern5(n)


'''Learnng Point:
1. You can use if else logic to execute print statements that will generate *'s based on the row they are being printed on.

(Ver1.0)

def pattern5(n):
    #Upper diamond
    #Outer loop is for the number of rows in the pattern.
    for i in range(1,n+1):
        #Inner loop for the number of columns for each row.
        for j in range(i):
            print("*",end="")
        print()
    for i in range(1, n):
        for j in range(n-i):
            print("*",end="")
        print()
'''