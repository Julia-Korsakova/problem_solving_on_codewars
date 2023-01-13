def printer_error(s):
    set_symbol = 'abcdefghijklm'
    set_s = set(s)
    errors = set_s.difference(set_symbol)
    count_errors = 0
    for i in errors:
        count_errors = count_errors + s.count(i)
    return f'{count_errors}/{len(s)}'
