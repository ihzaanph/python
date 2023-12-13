try:
    num = int(input("Enter a number: "))
    assert num >= 0, "Negative number"
except AssertionError as ae:
     print('Error :',ae)
