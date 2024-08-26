def disVowel(string_):
    newArr = []
    for i in string_:
        if i.lower() not in "aeiou":
            newArr.append(i)
    return ''.join(newArr)
    
    