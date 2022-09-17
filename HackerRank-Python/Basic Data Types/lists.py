if __name__ == '__main__':
    N = int(input().strip())
    
    L = []
    for i in range(N):
        args = input().strip().split(" ")
        if args[0] == "print":
            print(L)
        elif len(args) == 3:
            getattr(L, args[0])(int(args[1]), int(args[2]))
        elif len(args) == 2:
            getattr(L, args[0])(int(args[1]))
        else:
            getattr(L, args[0])()          


''' Learning Point:
1. You cannot use :
args = input().split(" ").strip() because after input() the split(" ") makes your input a list. You cannot use strip() on a collection like list. If you want to you need to iterate it and spply strip() on each of its element.

Instead you should use:
args = input().strip().split(" ")

2. Whenever you read an input using input(), get into the habit of applying strip() on it to get rid of non-printable characters. Example:

arg = input().strip()

3. Usage of getatttr(Object, Function) (Vars): Note that everything in python is an object. You can call a function using a name stored in a variable using getattr(). The Function should be present in the object. That's why we have a separate case of print() in the code using getattr() approach since print() is not an attribute of list object.

4. You can initialize an empty list in two ways:
    1. arr = list()
    2. arr = []

5. Read about list methods here: https://www.hackerrank.com/challenges/python-lists/tutorial 
'''

'''Previous Versions:

(Ver 1.0)
if __name__ == '__main__':
    N = int(input().strip())
    
    L = []
    for i in range(N):
        args = input().strip().split(" ")
        if args[0] == "insert":
            L.insert(int(args[1]),int(args[2]))
        elif args[0] == "print":
            print(L)
        elif args[0] == "remove":
            L.remove(int(args[1]))
        elif args[0] == "append":
            L.append(int(args[1]))
        elif args[0] == "sort":
            L.sort()
        elif args[0] == "pop":
            L.pop()
        elif args[0] == "reverse":
            L.reverse()  


'''