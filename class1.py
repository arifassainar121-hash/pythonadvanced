# class person:
#     def __init__(self):
#         self.name=input("enter the name: ")
#         self.age=input("enter the age: ")
#     def show(self):
#         print(self.name)
#         print(self.age)
# p1=person()
# p1.show()
# p2=person()
# p2.show()
from unittest import enterModuleContext


# class Employe:
#     def __init__(self):
#         self.emid=input('enter id: ')
#         self.name=input('enter name: ')
#         self.age=input('enter age: ')
#         self.designation=input('enter designation: ')
#
#     def getsalary(self):
#         print('salary',self.salary)
#
#
#     def showpersanaldetails(self):
#         print('employee id',self.emid,'name'self.name)
#     # def show(self):
#     #     print(self.emid)
#     #     print(self.name)
#     #     print(self.age)
#     #     print(self.designation)
# e1=Employe()
# e1.getsalary()
# e1.showpersanaldetails()



# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# #
# getarea() – to calculate and display the area of the circle.
# class circle:
#     def __init__(self):
#         self.radius=float(input('enter the radius: '))
#     def showarea(self):
#         print('The area: ',(self.radius**2)*3.14)
# c1=circle()
# c1.showarea()
#
#
# # getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# class circle:
#     def __init__(self):
#         self.perimeter=float(input('enter the radius: '))
#     def showarea(self):
#         print('The area: ',self.perimeter*2*3.14)
# c1=circle()
# c1.showarea()

# Create an object of the Circle class and call both methods to display the results.

# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:

# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance


#
# class Amount:
#
#   def __init__(self):
#     self.account = int(input("Enter your account no: "))
#     self.name = input("Enter your name: ")
#     self.balance = int(input("Enter your balance: "))
#
#   def withdraw(self):
#     amt = int(input("Enter withdrawal amount: "))
#     if amt <= self.balance:
#       self.balance=self.balance+amt
#       print("Withdrawal successful! New balance", self.balance)
#     else:
#       print("Insufficient balance.")
#
#   def deposit(self):
#     amt = int(input("Enter deposit amount: "))
#     self.balance += amt
#     print(f"Deposit successful! New balance: {self.balance}")
#
#   def show_balance(self):
#     print(
#         f"Account: {self.account} | Name: {self.name} | Balance:"
#         f" {self.balance}"
#     )
#
#
# accounts = []
#
# while True:
#   print("\n1. Create an account")
#   print("2. Withdraw")
#   print("3. Deposit")
#   print("4. Show balance")
#   print("5. Exit")
#
#   ch = int(input("Enter your choice: "))
#
#   if ch == 1:
#     a = Amount()
#     accounts.append(a)
#     print("Account created successfully!")
#
#   elif ch == 2:
#     number = int(input("Enter the account no: "))
#
#     for i in accounts:
#       if i.account == number:
#         i.withdraw()
#
#         break
#     if not found:
#       print("Invalid account number.")
#
#   elif ch == 3:
#     number = int(input("Enter the account no: "))
#
#     for i in accounts:
#       if i.account == number:
#         i.deposit()
#
#         break
#     if not found:
#       print("Invalid account number.")
#
#   elif ch == 4:
#     number = int(input("Enter the account no: "))
#     for i in accounts:
#       if i.account == number:
#         i.show_balance()
#         break
#     if not found:
#       print("Invalid account number.")
#
#   elif ch == 5:
#     print("Exiting application...")
#     break
#   else:
#     print("Invalid choice, please try again.")


#
# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class student:
    def __init__(self):
        self.name=input('enter student name: ')
        self.rollno=int(input('enter roll no : '))
        self.marks=int(input('enter marks : '))

    def show(self):
        print(self.name,self.rollno,self.marks)

    def updatemark(self):
        self.mark=int(input(('enteer mark: ')))


d=[]
while 1:
    print('1.add student')
    print('2.update mark ')
    print('3.print all student details')
    print('4.Search Student Roll Number')
    print('5.Delete Student')
    print('6.Exit')

    choice=int(input('enter choice : '))

    if choice==1:
        s=student()
        d.appent()

    elif choice==2:
        number=int(input('enter the roll no : '))
        for i in d:
            if(i.rollnonumber):
                i.update_mark()
                break
        else:
            print('invalid choice')
    elif choice==3:
        for i in d:
            i.display()
    elif choice==4:
        number=int(input('enter the no : '))
        for i in d:
            if(i.rollno==m=number)
                print('')


s=student()
s=show()





