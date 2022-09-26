'''
Pattern
    *********
     *******
      *****
       ***
        *

'''

def pattern9(n):
    #Outer loop is for the number of rows in the pattern.
    for i in range(1, n+1):
        print(" "*(i-1),end="")
        print("*"*(2*(n-i)+1),end="")
        print()

n = int(input().strip())
pattern9(n)