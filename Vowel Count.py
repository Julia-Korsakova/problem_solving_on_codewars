def get_count(sentence):
    vowel = 'euioa'
    return sum([sentence.count(i) for i in vowel])

