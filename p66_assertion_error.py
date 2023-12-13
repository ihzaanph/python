try:
    value = int(input("Enter a number: "))
    assert value >= 0, "Input cannot be negative"
    print("Input is valid and non-negative.")
except AssertionError as e:
    print("AssertionError:",e)

