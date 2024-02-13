class person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")


teacher = person("John", 34, "male")
accountant = person("Mary", 24, "female")
doctor = person("Joe", 25, "male")

print(teacher.firstname, teacher.age, teacher.gender)
print(accountant.firstname, accountant.age, accountant.gender)
print(doctor.firstname, doctor.age, doctor.gender)
teacher.details()