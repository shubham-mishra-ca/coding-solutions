'''
Pattern

     * * * * *
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *
     * * * * *

'''

def pattern12(n):
    for i in range(1, (2*n)+1):
        if i<=n:
            print(" "*(i-1),end="")
            print("* "*(n-i+1),end="")
            print()
        else:
            print(" "*((2*n)-i),end="")
            print("* "*(i-n),end="")
            print()


n= int(input().strip())
pattern12(n)