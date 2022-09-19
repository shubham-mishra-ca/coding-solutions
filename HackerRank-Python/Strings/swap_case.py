def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''Learning Point:

(Ver 1.0)

def swap_case(s):
    new_s = ''
    for i in s:
        if i.islower():
            new_s += i.upper()
        else:
            new_s += i.lower()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''