# class parent:
#     def m1(self):
#         print('paeent class method m1: ')
#     def m2(self):
#         print('parent method m2:')
#
# class child(parent):
#     def m3(self):
#         print('child class method m3: ')
#
#     # def m1(self):     #method overriding
#     #     print('child methof m1')
#     def m1(self):
#         super().m1()
#         print('child method m1:')
#
# c=child()
# c.m1()



# class person:
#     def __init__(self):
#         self.name=input('name: ')
#         self.age=input('age: ')
#
#     def show(self):
#         print('name',self.name,'age',self.age)
#
# class student(person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input('enter the roll no: '))
#         self.mark=int(input('enter the mark: '))
#
#     def show(self):
#         super().show()
#         print('rollno',self.rollno,'mark',self.mark)
#
#     def updatemark(self):
#         self.mark=int(input('enter new mark: '))
#
# s=student()
# s.show()
# s.updatemark()






# class category:
#     def __init__(self):
#         self.categary_name=input('enter the name: ')
#
#     def show(self):
#         print('cataegory',self.categary_name)
#
#
# class product(category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input('enter the product name: ')
#         self.price=int(input('enter the price: '))
#         self.quantity=int(input('enter the quantity: '))
#
#     def total_price(self):
#         print('total',self.quantity*self.price)
#
# c=category()
# c.show()
# c.total_price()
#
# #


# class comapny:
#     def _init__(self):
#         self.name=input('enter company name: ')
#         self.location=input('enter company location:')
#
#     def display(self):
#         print('company name: ',self.name,'company location: 'self.location)
#
#
# class employee(comapny):
#     def _init__(self):
#         super().__init__()
#         self.emid=input('enter employee id: ')
#         self.name=input('enter employee name: ')
#         self.salary=input('enter employee salary: ')
#
#     def display_company(self):
#         super().display_company()
#         print(self.emid,self.name,self.salary)
#         def update_salary(self):
#             self.salary=self.salary+(self.salary*0.1)
#             print("update salary",self.salary)
#
# s=employee()
# s.display_company()


