# experiment lng to ma'am. I'm not late. I passed on time huhu

def menu():
    while True:
        choice = input("1 Octal to Decimal\n2 Decimal to Octal\n3 Exit\n\nPlease enter the designated number for a certain task: ")
        if choice == "1":
            digit = input("Enter a string of octal digits: ")

            if "8" in digit or "9" in digit or not digit.isnumeric():
                print("Please input a valid octal value\n")

            else:
                digit = int(digit)
                i = 1
                decimal = 0

                while digit != 0:
                    remainder = digit % 10
                    digit //= 10
                    decimal += remainder * i

                    i *= 8

                print("The integer value is ", decimal, "\n")
        elif choice == "2":
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

                print('The octal representation is ', octal, "\n")

            else:
                print("Please input valid decimal value\n")

        elif choice == "3":
            break

        else:
            print("Please input a valid number\n")


menu()
