print("BASIC CALCULATOR!!")
a = float(input("Enter 1st Number: "))
b = input("Enter operand(+,-,*,/): ")
c = float(input("Enter 2nd Number: "))
if b == "+":
    print("Sum= ", a + c)
elif b == "-":
    print("Difference= ", a - c)
elif b == "*":
    print("Product= ", a * c)
elif b == "/":
    print("Quotient= ", a / c)
else:
    print("invalid operand!!")
