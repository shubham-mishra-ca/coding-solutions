'''
Pattern
     *****
      ****
       ***
        **
         *
'''

def pattern7(n):
    #Outer loop is for the number of rows in the pattern.
    for i in range(1,n+1):
        #Inner loop for the number of columns for each row.
        for j in range(i):
            print(" ",end="")
        for k in range(n-i+1):
            print("*",end="")
        print()


n = int(input().strip())
pattern7(n)