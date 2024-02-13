class employee:
    def __init__(self, name, salary):
        # public member
        self.name = name
        # Private member
        # not accessible outside of a class
        self._salary = salary

    def show(self):
        print("Name is", self.name, "and salary is", self._salary)


emp = employee("John", 40000)
emp.show()
# Access salary from outside of a class
print(emp._salary)
