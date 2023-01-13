def points(games):
    r = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            r = r + 3
        elif int(i[0]) < int(i[2]):
            r = r + 0
        elif int(i[0]) == int(i[2]):
            r = r + 1
    return r
