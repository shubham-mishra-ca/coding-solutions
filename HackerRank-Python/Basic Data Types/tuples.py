n = int(input().strip())
numbers = [int(num) for num in input().split(" ", n-1)]
print(hash(tuple(numbers)))


'''Learning Point:
Note: This challenge has some issues since running the same code on a diffrent website gives the hash as expected by the compiler. But on Hackerrank it's different. For now conider the solution above as the final and correct way of doing this challenge.

1. In Python3(CPython)cannot convert map object to tuple directly, it needs to be converted to a list first. But in PyPy you can directly convert a map to tuple.

2. List comprehension is the perfect way to take multiple inputs in a single line. The second parameter of split is maxsplit which means how many times do you want the split to work.


(Ver 1.0)
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

'''