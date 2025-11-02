a = eval(input("Enter a number: "))
b = eval(input("Enter another number: "))
opr = input("Choose an operation(+,-,*..../): ")
if opr == "+":
    print(a + b)
elif opr == "-":
    print(a - b)
elif opr == "*":
    print(a * b)
elif opr == "/":
    print(a / b)
elif opr == "//":
    print(a // b)
elif opr == "**":
    print(a ** b)
elif opr == "%":
    print(a % b)
else:
    print("Invalid input")

