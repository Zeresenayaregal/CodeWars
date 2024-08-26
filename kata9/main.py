def move_zeros(lst):
    lst2 = [i for i in lst if i != 0]
    lst2.extend([0] * lst.count(0))
    return lst2