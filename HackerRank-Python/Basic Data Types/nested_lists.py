if __name__ == '__main__':
    class_students= []
    marks_tracker = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        class_students.append([score, name])
        marks_tracker.add(score)
    
    # If there's more than 1 element in the set.
    if len(marks_tracker) > 1:
        second_lowest = sorted(marks_tracker)[1]
    else:
        #If there is only 1 element in the set.
        second_lowest = score
    
    #Iterate through the list and print the names corresponding to second lowest score.
    for score, name in sorted(class_students, key = lambda x:x[1]):
        if score == second_lowest:
            print(name)



'''Learning Point:
1. You already know how to traverse a nested list using nested for loops. But in situations like these where you want to access and compare a specific index of a list you use the format as seen while appending names to print_list.

    for score, name in class_students:
        if score == second_lowest:
            print_list.append(name)

This approach saves me from using nested loops.

2. To sort a nested list based on second parameter of each list we use lambda functions in key as shown : sorted(class_students, key = lambda x:x[1])

(Ver 1.0)
if __name__ == '__main__':
    class_students= []
    marks_tracker = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        class_students.append([score, name])
        marks_tracker.add(score)
    
    # If there's more than 1 element in the set.
    if len(marks_tracker) > 1:
        second_lowest = sorted(marks_tracker)[1]
    else:
        #If there is only 1 element in the set.
        second_lowest = score
    
    #Iterate through the list and print the names corresponding to second lowest score.
    print_list = []

    for score, name in class_students:
        if score == second_lowest:
            print_list.append(name)
    
    print_list.sort()
    
    for i in print_list:
        print(i)
'''