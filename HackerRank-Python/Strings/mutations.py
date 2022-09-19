def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

'''Learning Point:
1. There are other ways to do this. One that is discussed in Hackerrank tutarial is
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

However, this version has a lot of calls and is less efficient and more verbose.

2. Another way to take multiple inputs in a single line - i, c = input().split()
'''
