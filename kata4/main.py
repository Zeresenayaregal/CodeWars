def digital_root(n):
    numbers = [int(num) for num in str(n)]
    sum = 0
    for i in numbers:
        sum += i
    if sum > 9:
        return digital_root(sum)
    else:
        return sum

print(digital_root(132189))