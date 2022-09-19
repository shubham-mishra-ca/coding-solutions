def wrap(string, max_width):
    return "\n".join([ string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

'''Learning Point:
1. There is a textwrap module that needs to be imported. 2 functions in particular fill() and wrap()
 have features that makes a line width character in length. More on that here - https://www.hackerrank.com/challenges/text-wrap/tutorial

(Ver 1.0)
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
 
 '''
