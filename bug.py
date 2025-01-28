def function_with_uncommon_error(x, y):
    if x == 0:
        return y / x  # ZeroDivisionError if x is 0
    else:
        return x + y