'''
Pattern
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
'''

def pattern4(n):
    #Outer loop is for the number of rows in the pattern.
    for i in range(1,n+1):
        #Inner loop for the number of columns for each row.
        for j in range(1,i+1):
            print("{}".format(j),end="")
        print()


n = int(input().strip())
pattern4(n)