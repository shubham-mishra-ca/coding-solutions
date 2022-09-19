if __name__ == '__main__':
    s = input()
    string_functions = [str.isalnum, str.isalpha, str.isdigit,str.islower, str.isupper]
    for i in string_functions:
        print(any(map(i, s)))


'''Learning Point:
1. any() takes an iterable as parameter and return if any of it is true. Documentation - https://www.w3schools.com/python/ref_func_any.asp
2. I had a doubt how str is used in the way it is in string_functions list. Why does it work with str and not some random variable like x? Answer to that is that it is a  built in function. A comprehensive list can be found here - https://docs.python.org/3/library/functions.html

Also refer to this thread to clarify the doubt - https://stackoverflow.com/questions/1180303/static-vs-instance-methods-of-str-in-python

'''