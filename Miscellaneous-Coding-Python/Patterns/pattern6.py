'''
Pattern
         *
        **
       ***
      ****
     *****
'''

def pattern6(n):
    #Outer loop is for the number of rows in the pattern.
    for i in range(1,n+1):
        #Inner loop for the number of columns for each row.
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()


n = int(input().strip())
pattern6(n)