if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    print([ [i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n])



'''Learning Point:
1. Refer this Hackerrank tutorial to see all the variations how list comprehension is used. https://www.hackerrank.com/challenges/list-comprehensions/tutorial 

2. There are ways to reduce input calls:
    1. Concise, One-liner - x,y,z,n = int(input()), int(input()), int(input()), int(input())
    2. Efficient, less calls, one-liner - x, y, z, n = (int(input()) for _ in range(4))

(Ver 1.0)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([ [i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n])

'''