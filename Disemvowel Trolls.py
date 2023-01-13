def disemvowel(string_):
    text = list(string_)
    for i in text[::-1]:
        if i in 'euioaEUIOA':
            text.remove(i)
    return str(''.join(text))
