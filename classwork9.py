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

# class student:
#     def __init__(self):
#         self.name = input('enter student name: ')
#         self.rollno = int(input('enter roll no : '))
#         self.marks = int(input('enter marks : '))
#
#     def show(self):
#         print(self.name, self.rollno, self.marks)
#
#     def updatemark(self):
#         self.mark = int(input(('enteer mark: ')))
#
#
# d = []
# while 1:
#     print('1.add student')
#     print('2.update mark ')
#     print('3.print all student details')
#     print('4.Search Student Roll Number')
#     print('5.Delete Student')
#     print('6.Exit')
#
#     choice = int(input('enter choice : '))
#
#     if choice == 1:
#         s = student()
#         d.appent()
#
#     elif choice == 2:
#         number = int(input('enter the roll no : '))
#         for i in d:
#             if (i.rollno == m=number)
#                 i.update_mark()
#                 break
#         else:
#             print('invalid choice')
#     elif choice == 3:
#         for i in d:
#             i.display()
#     elif choice == 4:
#
#
#
#         number = int(input('enter the roll no : '))
#         for i in d:
#             if i.rollno == number:
#                 print("Student Found:")
#                 i.display()
#                 break
#         else:
#             print('Student not found.')
#
#     elif choice == 5:
#         number = int(input('enter roll no to delete: '))
#         for i in d:
#             if i.rollno == number:
#                 d.remove(i)
#                 print("Student removed successfully.")
#                 break
#         else:
#             print('Student not found.')
#
#         elif choice == 6:
#         print("Exiting program.")
#         break
#
#        else:
#         print("Invalid choice, please select between 1 and 6.")



class Student:
    def __init__(self):
        self.name = input('Enter student name: ')
        self.rollno = int(input('Enter roll no: '))
        self.marks = int(input('Enter marks: '))

    def display(self):
        print(f"Name: {self.name} | Roll No: {self.rollno} | Marks: {self.marks}")

    def update_mark(self):
        self.marks = int(input('Enter new marks: '))
        print("Marks updated successfully.")


d = []
while True:
    print('\n1. Add Student')
    print('2. Update Mark')
    print('3. Print All Student Details')
    print('4. Search Student Roll Number')
    print('5. Delete Student')
    print('6. Exit')

    choice = int(input('Enter choice: '))

    if choice == 1:
        s = Student()
        d.append(s)

    elif choice == 2:
        number = int(input('Enter the roll no: '))
        for i in d:
            if i.rollno == number:
                i.update_mark()
                break
        else:
            print('Roll number not found.')

    elif choice == 3:
        if not d:
            print("No student records available.")
        for i in d:
            i.display()

    elif choice == 4:
        number = int(input('Enter the roll no: '))
        for i in d:
            if i.rollno == number:
                print("Student Found:")
                i.display()
                break
        else:
            print('Student not found.')

    elif choice == 5:
        number = int(input('Enter roll no to delete: '))
        for i in d:
            if i.rollno == number:
                d.remove(i)
                print("Student removed successfully.")
                break
        else:
            print('Student not found.')

    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please select between 1 and 6.")
