def function_with_error_handling(x, y):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = y / x
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        return x + result