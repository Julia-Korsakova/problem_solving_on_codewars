def high_and_low(numbers):
    new_list = numbers.split()
    new_int_list = list(map(int, new_list))
    return f'{max(new_int_list)} {min(new_int_list)}'
