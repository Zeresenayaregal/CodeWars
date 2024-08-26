def dig_pow(n, p):
    lisNum = list(str(n))
    total = 0
    for j in lisNum:
            total += int(j)**p
            p += 1
    if total%n == 0:
        return total//n
    else:
        return -1

print(dig_pow(695, 2))