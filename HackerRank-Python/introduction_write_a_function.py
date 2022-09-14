def is_leap(year):
    return year%4 ==0 and (year%100!=0 or year%400==0)

year = int(input())
print(is_leap(year))


"""Learning Point:
Never use if-else if you\'re just return boolean value. An efficient solution is to write it in a boolean statement. 
However note that this may not be readable if the boolean expression is complex. Don't write redundant code(one that is unnecessary and never executes) be DRY(Don't Repeat Yourself).

So instead of writing this
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 ==0:
        leap = True
    return leap


You should do something like this: (See current code)


"""