def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i, width=width))
  
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



'''Learning Point:
1. Refer to this link for learning more on python format() - https://pyformat.info/ 

2. Refer to this link to learn more about placeholder values {} - https://www.w3schools.com/python/ref_string_format.asp 

3. 
'''
