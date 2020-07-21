def no_dups(s):
    s = s.split()
    new_s = []
    duplicates = {}
    for word in s:
        if word not in duplicates:
            duplicates[word] = 1
            new_s.append(word)
    result = " ".join(new_s)
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
