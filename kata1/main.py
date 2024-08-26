def length_of_sequence(arr,n):
    occrArr= []
    i = 0
    while True:
        try:
            pos = arr.index(n, i)
            occrArr.append(pos)
            i = pos + 1
        except ValueError:
            break
    
    if(len(occrArr) < 2 or len(occrArr) > 2):
        return 0
    newArr = arr[occrArr[0]:occrArr[1]+1]
    
    return len(newArr)


print(length_of_sequence([1, 3, 4, 5, 4, 6, 7, 4, 6, 3],))