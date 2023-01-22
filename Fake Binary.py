def fake_bin(x):
    # res = ''
    # list_s = list(x)
    # for i in list_s:
    #     if int(i) < 5:
    #         res += '0'
    #     elif int(i) >= 5:
    #         res += '1'
    # return res

    return ''.join('0' if i < '5' else '1' for i in x)
