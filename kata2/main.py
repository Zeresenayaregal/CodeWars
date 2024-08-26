def count_bits(n):
    binary_form = format(n, 'b')
    count = 0
    for i in binary_form:
        if i == '1':
            count += 1
        else:
            continue
    return count