# Inbuilt functions
number = max(34, 78, 90, 123, 45)
print(number)

y = min(45, 78, 34, 23)
print(y)

z = pow(2, 3)
print(z)


# User-defined functions
def name():
    print("John")


name()  # Calling a function


def details():
    noir = "Aziz"
    age = 18
    course = "MIT"
    print(name, age, course)


details()


# Parameters/variables an arguments
def patient(name, gender, age,  marriageStatus):
    print(name, gender, age, marriageStatus)


patient("Job", "Female", "45", "married")
patient("Mary", "female", "34", "not married")


def multiply(x, y):
    print(x * y)


multiply(2, 6)
multiply(9, 18)
multiply(18, 40)
multiply(10, 35)

# Create a user-defined fuctions
# Called employees. Display details of
# five employees using the
# following parameters: fullname,age
# position, salary
def employees(fullname, age, position, salary):
    print(fullname, age, position, salary)

employees("Mark Mwongoni","31", "Secretary", "30,000" )
employees("Judy Wamocii","51", "Supervisor", "100,000" )
employees("Joseph Mbugua","41", "Manager", "130,000" )
employees("Antony Kimani","26", "Accountant", "60,000" )
employees("Caroline Mutuku","37", "Chef", "90,000" )