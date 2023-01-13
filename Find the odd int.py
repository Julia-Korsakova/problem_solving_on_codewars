def find_it(seq):
    new_list = list(set(seq))
    for i in new_list:
        if seq.count(i) % 2 != 0:
            return i
