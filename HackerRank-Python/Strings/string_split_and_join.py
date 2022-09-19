def split_and_join(line):
    return line.replace(" ", "-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


'''Learning Point:
1. split() and join() are great way to do this but a better way that has a single call is using replace(). More on that here - https://www.w3schools.com/python/ref_string_replace.asp 

(Ver 1.0)
def split_and_join(line):
    return "-".join((line.split(" ")))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
'''