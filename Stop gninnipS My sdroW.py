def spin_words(sentence):
    new_list = []

    list_word = sentence.split(' ')

    for word in list_word:
        if len(word) >= 5:
            r_word = word[::-1]
            new_list.append(r_word)
        else:
            new_list.append(word)

    return ' '.join(new_list)
