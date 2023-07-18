def IfPolindrom(word):
    counter = 1
    a = True
    for i in range(0, len(word)//2):
        if word[i] != word[i - counter]:
            a = False
        counter += 2
    return a