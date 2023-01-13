def sum_array(arr):
    if arr is None:
        return 0
    elif len(arr) == 0 or len(arr) == 1:
        return 0
    elif len(arr) != 0:
        return sum(arr) - min(arr) - max(arr)
