def solution(numbers):
    arr = [0,1, 2, 3,4,5,6,7,8,9];a=0
    for i in range(len(arr)):
        if arr[i] not in numbers:
            a += arr[i]
    return a     
