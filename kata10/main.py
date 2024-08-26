def disemvowel(string_):
    newStr = []
    for i in string_:
        match i.lower():
            case 'a'|'e'|'i'|'o'|'u':
                continue;
            case _:
                newStr.append(i)
    return "".join(newStr)