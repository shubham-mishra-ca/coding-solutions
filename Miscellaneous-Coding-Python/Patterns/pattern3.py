'''
Pattern
    *****
    ****
    ***
    **
    *
'''


def pattern3(n):
    #Outer loop is for the number of rows in the pattern.
    for i in range(1,n+1):
        #Inner loop for the number of columns for each row.
        for j in range(n+1-i,0,-1):
            print("*",end="")
        print()


n = int(input().strip())
pattern3(n)