'''Pattern
     * * * * *
      * * * *
       * * *
        * *
         *
'''

def pattern11(n):
    for i in range(1,n+1):
        print(" "*(i-1),end="")
        print("* "*(n-i+1),end="")
        print()

n = int(input().strip())
pattern11(n)