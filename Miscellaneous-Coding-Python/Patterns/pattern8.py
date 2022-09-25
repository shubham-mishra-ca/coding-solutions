'''
Pattern
        *
       ***
      *****
     *******
    *********
'''

def pattern8(n):
    #Outer loop is for the number of rows in the pattern.
    for i in range(n+1):
        #Inner loop for the number of columns for each row.
        for j in range((n-i)//2):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        for l in range((n-i)//2,n+1):
            print("*"*(i-1))
        print()

n = int(input().strip())
pattern8(n)