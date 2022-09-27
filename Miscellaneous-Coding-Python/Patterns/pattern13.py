'''
Pattern

         *
        * *
       *   *
      *     *
     *********
'''

def pattern13(n):
    for i in range(1,n+1):
        if i == n:
            stars = (2*n)-1
        else:
            stars = i
        for j in range(n+1-i):
            print(" ",end="")
        if i == 1 or i == n:
            for k in range(stars):
                print("*",end="")
        else:
            print("*"+" "*((2*i)-3)+"*",end="")
        print()


n = int(input().strip())
pattern13(n)