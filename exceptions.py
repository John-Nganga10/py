try:
    print(x)
except:
    print("Name error occured")

try:
    num1 = 20
    num2 = 10
    print(num1 / num2)
except:
    print("Zero division error occured")
finally:
    print("success")

# User-defined function
try:
    def sum(first, second):
        return first + second
except:
    print("ExCeptions occured")
finally:
    print("success")
print(sum(10, 29))
