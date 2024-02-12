# Area of a rectangle - A = length * width
length = int(input("Enter length:"))
width = int(input("Enter width:"))
print(length * width)
print("The area is", length * width)

# Perimeter of a rectangle - 2(length + width)
len = int(input("Enter length:"))
wid = int(input("Enter width:"))

perimeter = 2*(len + wid)
print("The perimeter is", perimeter)

# Assignment
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
oper = input("Enter operator")
if oper == '+':
    print("Result", num1+num2)

elif oper == '-':
    print("Result", num1-num2)
elif oper == '*':
    print("Result", num1*num2)
elif oper == '/':
    print("Result", num1/num2)
else:
   print("Invalid operator")