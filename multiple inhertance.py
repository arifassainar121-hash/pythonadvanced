# class hospital:
#     def __init__(self):
#         self.hospital_name=input('enter the hospital name: ')
#         self.hospital_location=input('enter the location of hospital: ')
#         self.hospital_phno=input('enter the phone number of hospital: ')
#
#     def display_hospital(self):
#         print('hospital_name',self.hospital_name)
#         print('hospotal_loaction',self.hospital_location)
#         print('hospital_phno',self.hospital_phno)
# class department:
#     def __init__(self):
#         self.department_name=input('enter the department name: ')
#         self.doctor_name=input('enter the doctor name: ')
#     def display_department(self):
#         print('department_name',self.department_name)
#         print('doctor_name',self.doctor_name)
# class patient(hospital,department):
#     # hospital().__init__(self),department().__init__(self)
#     def __init__(self):
#         self.patient_name=input('enter the patient name: ')
#         self.patent_age=int(input('enter the paitent age: '))
#         self.patient_phone=int(input('enter the patient phone  number: '))
#         self.patient_admission_date=int(input('enter the patient admission date: '))
#         self.patient_discharge_date=int(input(''))
#
#
#
#     def dischage_data(self):
#         print('patient_discharge_date',self.patient_discharge_date)
#
#     def full_summary(self):
#         hospital.display_hospital()
#         department.display_department()
#         print('patient_name',self.patient_name)
#         print('patient_age',self.patient_age)
#         print('patient_phone',self.patient_phone)
#         print('patient_admission_date',self.patient_admission_date)
#         print('patient_discharge_date',self.patient_discharge_date)
#         if(self.dischage_data==""):
#             print('patient not discharged')
#         else:
#             print('patient discharged',self.patient_discharge_date)
#
# p=hospital()
# p.full_summary()
# p.discharge_date()



#
# class Hospital:
#
#   def __init__(self):
#     self.hospital_name = input("Enter the hospital name: ")
#     self.hospital_location = input("Enter the location of hospital: ")
#     self.hospital_phno = input("Enter the phone number of hospital: ")
#
#   def display_hospital(self):
#     print("Hospital Name:", self.hospital_name)
#     print("Hospital Location:", self.hospital_location)
#     print("Hospital Phone:", self.hospital_phno)
#
#
# class Department:
#
#   def __init__(self):
#     self.department_name = input("Enter the department name: ")
#     self.doctor_name = input("Enter the doctor name: ")
#
#   def display_department(self):
#     print("Department Name:", self.department_name)
#     print("Doctor Name:", self.doctor_name)
#
#
# class Patient(Hospital, Department):
#
#   def __init__(self):
#     Hospital.__init__(self)
#     Department.__init__(self)
#
#     self.patient_name = input("Enter the patient name: ")
#     self.patient_age = int(input("Enter the patient age: "))
#     self.patient_phone = input("Enter the patient phone number: ")
#     self.patient_admission_date = input(
#         "Enter the patient admission date (YYYY-MM-DD): "
#     )
#     self.patient_discharge_date = input(
#         "Enter the patient discharge date (or leave empty if not discharged): "
#     )
#
#   def discharge_data(self):
#     print("Patient Discharge Date:", self.patient_discharge_date)
#
#   def full_summary(self):
#
#     self.display_hospital()
#     self.display_department()
#
#     print("Patient Name:", self.patient_name)
#     print("Patient Age:", self.patient_age)
#     print("Patient Phone:", self.patient_phone)
#     print("Patient Admission Date:", self.patient_admission_date)
#
#     if not self.patient_discharge_date:
#       print("Status: Patient not discharged")
#     else:
#       print("Status: Patient discharged on", self.patient_discharge_date)
#
#
# p = Patient()
# p.full_summary()
# p.discharge_data()
#


