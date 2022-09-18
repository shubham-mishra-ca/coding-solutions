if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum_marks = 0
    for i in student_marks[query_name]:
        sum_marks += i
    print(format(sum_marks/len(student_marks[query_name]),'.2f'))


'''Learning Point:
1. Neat way to take multiple inputs in one line
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))

2. To have the output as a decimal number with a precision of upto 2 decimal places we use the format() function.


'''