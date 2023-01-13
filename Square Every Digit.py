def square_digits(num):
    return int(''.join([str(int(i) ** 2) for i in list(str(num))]))

    # e = list(map(int, list(str(num))))
    # u = list(map(lambda i: i*i, e))
    # p = list(map(str, u))
    # return int(''.join(p))
