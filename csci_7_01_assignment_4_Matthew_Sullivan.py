# 1. Run this application repeatedly since we have seen While Loops
# 2. Allow the user to enter two numeric data values
# 3. Allow the user to select whether they wish to:
#     Add those two numbers
#     Subtract those two numbers
#     Multiply those two numbers
#     Divide the first number by the second number (if the denominator, second number, is zero, print an error message “Cannot Divide by Zero”
#     Display all of the above calculations, one function calling the other four functions
#     Raise the first number to the power of the second number (i.e. 4.5 2 or 3.43.3)
#     Quit


def addition(num1, num2):
    sum = num1 + num2
    return sum

def subtraction(num1, num2):
    sum = num1 - num2
    return sum

def multiplication(num1, num2):
    sum = num1 * num2
    return sum

def division(num1, num2):
    try:
        sum = num1/num2
        return sum
    except ZeroDivisionError:
        return 'Cannot divide by zero'

def power(num1, num2):
    sum = num1**num2
    return sum

replay = "y"
while (replay == "y"):

    print("\n\tOption #1 - Add Two Numbers")
    print("\tOption #2 - Subtract Two Numbers")
    print("\tOption #3 - Multiply Two Numbers")
    print("\tOption #4 - Divide Two Numbers")
    print("\tOption #5 - Raise One Number to the Power of a Second Number")
    print("\tOption #6 - ALL Calculations")
    print("\tOption #7 - Quit")

    user_choice = abs(int(input("\n\tEnter Option: 1, 2, 3, 4, 5, 6 or 7: ")))


    if user_choice == 7:
        print("\n\tProgram has ended")
        exit()


    number1 = float(input("\n\tEnter First Number: "))
    number2 = float(input("\tEnter Second Number: "))


    if user_choice == 1:
        print("\n\t%.2f + %.2f = %.2f"% (number1, number2, addition(number1, number2)))
    elif user_choice == 2:
        print("\n\t%.2f - %.2f = %.2f"% (number1, number2, subtraction(number1, number2)))
    elif user_choice == 3:
        print("\n\t%.2f X %.2f = %.2f"% (number1, number2, multiplication(number1, number2)))
    elif user_choice == 4:
        if isinstance(division(number1, number2), str):
            print("\n\t%.2f/%.2f = %s"% (number1, number2, division(number1, number2)))
        else:
            print("\n\t%.2f/%.2f = %.2f"% (number1, number2, division(number1, number2)))
    elif user_choice == 5:
        print("\n\t%.2f**%.2f = %.2f"% (number1, number2, power(number1, number2)))
    elif user_choice == 6:
        print("\n\t%.2f + %.2f = %.2f"% (number1, number2, addition(number1, number2)))
        print("\t%.2f - %.2f = %.2f"% (number1, number2, subtraction(number1, number2)))
        print("\t%.2f X %.2f = %.2f"% (number1, number2, multiplication(number1, number2)))
        if isinstance(division(number1, number2), str):
            print("\t%.2f/%.2f = %s"% (number1, number2, division(number1, number2)))
        else:
            print("\t%.2f/%.2f = %.2f"% (number1, number2, division(number1, number2)))
        print("\t%.2f**%.2f = %.2f"% (number1, number2, power(number1, number2)))

    replay = str(input("\n\tWould you like to rerun this program(Y/N): "))
    replay = replay.lower()
exit()
