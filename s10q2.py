class Employee:
    def input1(self):
        self.id = input("Enter your id:")

class Clerk:
    def input2(self):
        self.name = input("Enter your name:")
        self.sal = int(input("Enter your salary:"))

class Manager(Employee, Clerk):
    def view(self):
        super().input1()
        super().input2()

        print("\n\n=======Employee Details==========\n")

        print("Your id is:", self.id)
        print("Your name is:", self.name)
        print("Your salary is:", self.sal)

obj = Manager()
obj.view()