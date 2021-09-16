repeat = "yes"
while repeat.lower().strip() == 'yes':
    num1 = input("Enter number 1 here: ")
    sign = input("What do you want to do: ")
    num2 = input("Enter number 2 here: ")
    num1 = float(num1)
    num2 = float(num2)
    if sign == "+":
        then: print(num1 + num2)
    elif sign == "-":
        then: print(num1 - num2)
    elif sign == "/":
        then: print(num1 / num2)
    elif sign == "*":
        then: print (num1 * num2)
    else:
        then: print("This action is not supported")
    repeat=input("Do you want to perform another calculation? Yes or No? ")


