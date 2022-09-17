if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print("{0}\n{1}".format((a//b), a/b))

'''Learning Point:
1. Python has 2 types of division. 
    a. Integer division(//) - Provides floor value on division.
    b. Float division(/) - Provides exact value upto certain precision.

2. You should get into the habit of printing variables as in the current code and not like as shown in Ver 1.0. Check this link for documentation of format() - https://www.w3schools.com/python/ref_string_format.asp


(Ver 1.0)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
'''