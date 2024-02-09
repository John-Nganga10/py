temperature = 34
if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that determines  the largest number among three number
num1 = 80
num2 = 68
num3 = 39
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 47
if number % 2 == 0:
    print(number, "is even")
else :
    print(number, "is odd")

# A program that checks whether a number is a prime or not
p = 2
if p % 2 == 0 :
    print(p, "is not prime number")
elif p % 3 == 0 :
    print(p, "is not a prime number")
else :
    print(p, "is a prime number")

num = 17
if num > 1 :
    for x in range(2, num):
        if num % x == 0:
            print("Not prime")
        else :
            print("the number is prime")
            break
    else:
        print("The number is not a prime number")