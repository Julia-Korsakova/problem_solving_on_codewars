def comp(array1, array2):
    if array1 is not None and array2 is not None:
        array1 = sorted(list(map(lambda i: i ** 2, array1)))
        array2 = sorted(array2)
        return array1 == array2
    return False
