def narcissistic( value ):
    n = list(str(value))
    return sum([int(i)**len(n) for i in n]) == value