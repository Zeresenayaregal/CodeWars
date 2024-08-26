def find_missing_letter(chars):
    for i,c in enumerate(chars):
        if ord(chars[i])+1 == ord(chars[i+1]):
            continue
        else:
            return chr(ord(chars[i]) + 1)