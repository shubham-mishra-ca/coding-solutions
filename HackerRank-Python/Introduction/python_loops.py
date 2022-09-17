if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)

'''Learning Point:
1. range accepts 3 arguements at maximum and a minimum of 1. Syntax: range(start, stop, step) 
    range(5, -1, -1) produces the descending sequence from  through  and range(0, 5, 2) produces 0, 2, 4. If you are going to provide a step value, you must also include a start value.
'''