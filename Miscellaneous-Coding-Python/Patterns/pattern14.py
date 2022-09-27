'''
Pattern
     *********
      *     *
       *   *
        * *
         *
'''

def pattern14(n):
     for i in range(0, n):
          for j in range(0, 2*n-1):
               if i == 0:
                    print("*",end="")
               elif i == j or i+j == 2*n-2:
                    print("*",end="")
               else:
                    print(" ",end="")
          print()

n = int(input().strip())
pattern14(n)


'''Learning Point:
1. Sometimes using two loops look for patterns between row and column numbers. Here the stars are printed when row and column numbers are same or add to 2*n-2. 

'''