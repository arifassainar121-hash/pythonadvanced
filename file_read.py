# read  // return string format
# readlines \\ return string format
from zipimport import path_sep

#
# f=open("k.txt","r")
#
# s=f.readlines()
# print(s)
# print(type(s))
# f.close()



# #write a program to read a text file and displays the number of lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(len(s))
# #write a program to display the number of words in a file
# f=open('k.txt','r')
# s=f.read(len(s))
# print(s)

# # #write a program to update the second line in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(s)
# s[1]="new one\n"
# f.close()
#
# f=open('k.txt','w')
# f.writelines(s)
#
# f.close()




# Ensure the list has at least 2 items before modifying index 1




# #write a program to display the last 5 lines in a file


#
# f=open('k.txt','r')
# s=f.readlines()
# print(s[-5:])
# f.close()






#program to search a particular word in a file

# f=open('k.txt','r')
# s=f.read()
# n=input('enter the word: ')
# for i in s:
#     if i==n:
#         print('found')
#     else:
#         print('not found')
# f.close()

# f=open('k.txt','r')
# s=f.read()
# n=input('enter the word: ')
# if 'apple' in s:
#     print('found')
# else:
#     print('not found')
# f.close()


#find the number of letters,digits,and spaces in a file

# f=open('k.txt','r')
# s=f.read()
# l_count=0
# d_count=0
# s_cound=0
# for i in s:
#     if(i.isdigit()):
#         d_count+=1
#     if(i.isalpha()):
#         l_count+=1
#     if(i.isspace()):
#         s_cound+=1
#     else:
#         pass
# print(d_count,'digits')
# print(l_count,'letters')
# print(s_cound,'spaces')


# reverse the lines in a file

# f=open('k.txt','r')
# s=f.readlines()
# s.reverse()
# print(s)
#
# f=open('k.txt','r')
# s=f.readlines()
# print(s[::-1])
# f.close()
#
# f=open('k.txt','w')
# s=f.writelines(s)
# f.close()

# A file total_students.txt contains the names of all students in a class,
# and a file passed_students.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# Find the students who did not pass.
# Write their names to a new file named failed_students.txt, one name per line.
#
# f=open('student.txt','r')
# n=f.readlines()
# f=open('pass.txt','r')
# m=f.read()
# print('failed students are: ')
# for i in n:
#
#     if i not in m:
#         print(i)

#
# f=open('k.txt','a')

# f.write('python')
# f.close()






# append the content from one file to another file



# f=open('k.txt','a+')
# f.write('python')
# s=f.read()
# print(s)
#
# print('se cond position',f.tell())
# f.seek(0)
#
# print('third position',f.tell())
# s=f.read()
# print(s)
# f.close()




#
# while True:
#     print('1.file read')
#     print('2.file write')
#     print('3.file append')
#     print('4.file search')
#     print('5.file delete')
#     print('6.file exit')
#
#     c = int(input('enter your choice: '))
#
#     if c == 1:
#         filename=input("enter trhe name: ")
#         f=open('k.txt','r')
#         s=f.read()
#         print(s)
#         pass
#     elif c == 2:
#         pass
#     elif c == 3:
#         pass
#     elif c == 4:
#         pass
#     elif c == 5:
#         pass
#     elif c == 6:
#         break
#     else:
#         print("Invalid choice, please try again.")



    # if c==3:
    #     filename=input('enter file name')
    #     f=open(filename,'r')
    #     s=f.read()
    #     word=input('enter the file file to be searched')
    #     for i in s:
    #         if word in s :
    #             print(word,'is present')
    #         else:
    #             print(word,'is not present')





