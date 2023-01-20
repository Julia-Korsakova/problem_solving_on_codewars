def is_isogram(string):
# str_low = string.lower()
#     str_set = set(str_low)
#     print(str_set)
#     c = 0
#     for i in str_set:
#         t = str_low.count(i)
#         if t > 1:
#             c = c + 1
#     return False if c > 0 else True

    str_set = list(set(string.lower()))
    return True if len(string) == len(str_set) else False
