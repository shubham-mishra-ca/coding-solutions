if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_num = list(arr)
    maximum_number = max(list_num)
    while max(list_num) == maximum_number:
        list_num.remove(maximum_number)
    print(max(list_num))


'''Learning Point:

(Ver 1.0)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_num = list(arr)
    
    list_sorted = sorted(list_num, reverse = True)
    max = list_sorted[0]
    for i in list_sorted:
        if i < max:
            print(i)
            break

(Ver 2.0)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    set_num = set(arr)
    set_sorted = sorted(set_num, reverse = True)
    print(set_sorted[1])

'''