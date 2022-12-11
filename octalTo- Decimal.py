digit = input("Enter a string of octal digits: ")

if "8" in digit or "9" in digit or not digit.isnumeric():
    print("Please input a valid octal value")

else:
    digit = int(digit)
    i = 1
    decimal = 0

    while digit != 0:
        remainder = digit % 10
        digit //= 10
        decimal += remainder * i

        i *= 8

    print("The integer value is ", decimal)