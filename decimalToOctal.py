digit = input('Enter a decimal integer: ')

if digit.isnumeric():

    print("Quotient Remainder Octal")

    octal = 0
    i = 1
    num = ""

    while digit != 0:
        digit = int(digit)

        remainder = digit % 8
        digit //= 8
        octal = octal + remainder * i
        i *= 10
        num = str(remainder) + num

        print("%5d%8d%12s" % (digit, remainder, num))

    print('The octal representation is ', octal)

else:
    print("Please input valid decimal value")