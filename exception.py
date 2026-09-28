# def name():
#     try:
#         x=int(input('enter your age: '))
#
#     except Exception as r :
#         print(r)
#         name()   #recursion
#
#     finally:
#         print('finised')
#
# name()


# try:
#     n=int(input('enter your age: '))
#     if(n>18):
#         raise ValueError('not eligible for voting')
#     else:
#
#         print('your age is')
# except ValueError as e:
#     print(e)



class MyException(Exception):
    pass
    try:
        n = int(input('enter your age: '))
        if n < 18:
            raise MyException('not eligible for voting')
        else:
            print('you are eligible', n)

    except MyException as e:
        print('Error:', e)
    except ValueError:
        print('Please enter a valid numeric age.')



#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"



#Ask the user to enter a password.if its length is less than 8 characters,raise
# #a customexception InvalidPasswordError with the message ("Password should b ! # characters")

#Ask the user to enter an amount and if the amount<balance, raise customExcep
# #Insuffient BalanceError with the message("Not Enough Balance. Transaction Faile



#Ask the user to enter an amount and if the amount<balance,
# raise customExcep #Insuffient BalanceError with the message("Not Enough Balance. Transaction Faile

#Ask the user to enter an amount and if the amount<balance,
# raise customExcep #Insuffient BalanceError with the message("Not Enough Balance. Transaction Faile
