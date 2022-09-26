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
    for i in range(1,n+1):
        if i> 1:
            stars = (2*i) - 1
        else:
            stars = i
        for j in range(n+1-i):
            print(" ",end="")
        for k in range(stars):
            print("*",end="")
        print()
            
n = int(input().strip())
pattern8(n)