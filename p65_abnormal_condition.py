try:
    user_input = int(input("Enter an integer: "))
    if user_input < 90 or user_input > 120:
        raise ValueError('abnormal condition')
    else:
        print("Input value is within the range (90-120).")
except ValueError as ve:
    print("ValueError: ",ve)
