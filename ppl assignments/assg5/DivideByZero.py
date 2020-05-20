def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Divion By Zero Error")
    else:
        print("Result: ", result)
    finally:
        print("Program Over")

divide(2, 1)