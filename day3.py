# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter value of B:"))
#     print(a/b)
# except ZeroDivisionError:
#    print("canot be divisible by zero")
# except ValueError:
#    print("enter only enteger value")
#    print("continue")

#exception handling
# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except ZeroDivisionError:
#    print("plz ensure that you can't dividr any no by zero")
# except ValueError:
#    print("enter only integer no=>", message)


#handing multiple differnt kinf of exception with single except block
# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ValueError,ZeroDivisionError)as message:
#    print("message")



# we can requirement multiple exception then in sitution default except block       must be last
# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except:
#     print("this is default part of evcept block")
# except (ValueError,ZeroDivisionError)as message:
#    print("Enter correct number:",message)



# we can use else block if no error will genrate it is depwnd on our own need and neccessity
# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)

# except (ValueError,ZeroDivisionError)as message:
#    print("Enter correct number:",message)
# else:
#     print("Everything is ok")



# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ValueError,ZeroDivisionError)as message:
#    print("Enter correct number:",message)
# finally:
#     print("I will always excuted")


#nested try except block
# try:
#     a=int(input("Enter first  no:"))
#     b=int(input("Enter second no:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#          print("msg")
# except ValueError as msg:
#    print("msg")


# try:
#     a=int(input("Enter first  no:"))
#     b=int(input("Enter second no:"))
#     print(a/b)
# except(ZeroDivisionError,ValueError)as message:
#    print(message)
# else:
#    print("thee are no error in try block")
# finally:
#    print("i am finally block i always executed whether ")
   
# bank_bal=500
# if bank_bal<2000:
#     raise Exception("your account balance is below a accessable")
# else:
#     print("your amount has withdrawl")


#python logging 
# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# logging.debug("this indicate the debugging information")
# logging.info("this indicate the important inforamation")
# logging.error("this indicate the error information")
# logging.warning("this indicate the warning inforamation")
# logging.critical("this indicate the critiacl information")

# import logging
# logging.basicConfig(filename="arithmatic.txt",level=logging.DEBUG)
# try:
#     a=int(input("enter first integer no"))
#     b=int(input("enter second integer no"))
#     print(a/b)
# except(ZeroDivisionError,ValueError)as msg:
#     print(msg)
#     logging.exception(msg)
#     print("logging level is set up check 'arithmatic.txt for log details.")

    # write a program 3 paper marks like phy,chem,math and calculate total % and display total marks% and condition:
    #if user is passes in all sunject then print pass else print fail and passing marks is 40
    #if percentage is greater then qual to 65 and genter is male the print you are eligible for placement else not eligible for placement 

# class marks:
#     phy=int(input("enter phy marks:"))
#     chem=int(input("enter phy marks:"))
#     math=int(input("enter phy marks:"))
#     total=phy+chem+math
#     percentage=(total/300)*100
#     print("total marks=",total)
#     print("persentage=",percentage)
#     if phy>=40 and chem>=40 and math>=40:
#         print("pass")
#     else:
#         ("fail")


#     gender=input ("enter your gender male/female:")
#     if percentage >=65 and gender.lower()=="male":
#         print("elegible")
#     else:
#         print("not eligible")


#time complexity
#0(1)-constant time
# array={1,2,3,4}
# array[0]

# o(N)=linear time
# array={1,2,3,4,5}
# for element in array 
#     print(element)#linear tine since it is visiting element in array

#o(N)logarithmic time
# array={1,2,3,4,5}
# for  index in range(0,len(array),3)
#      print(array[index])   LT since it is visiting only some element/

# o(N^2)-Quadratic Time            N^2 Means looking ar a every index in the array twice
# array={1,2,3,4,5}
# for x in array:
#     for y in array:
#         print(x,y)

# O(2^N)-Exponential Time
# def fibonacci(n)
#     if n<=1;
#         return n
#     return fibonacci(n-1)+fibonacci(n-2)

# def add():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a+b)

# def sub():
#     a=int(input("enter value of A:"))
#     b=(input("enter value of B:"))
#     print(a-b)

# def div():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a/b)

# def mul():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a*b)


# while True:
#     print("1.Addition")
#     print("2.substraction")
#     print("3.division")
#     print("1.multipication")
#     print("5.exit")
#     choice=int(input("enter your choice:"))
#     if choice == 1:
#         add()#calling function
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         div()
#     elif choice == 4:
#         mul()
#     elif choice == 5:
#         sys.exit()

# array=[1,2,3,4]


#stack operation
# push
# pop 
# peek
#stack implementation with size limit



print('shreyadeore123'.isalnum())
print('shreyadeore'.isalpha())
print('777f'.isdigit())
print('sdsdsdsd'.islower())
print(''.islower())
print('shreyad'.isupper())
print('my name isshreyadeore'.istitle())
print(''.istitle())
print(''.isspace())
print('hello'.startswith("he"))
print('hello'.endswith("lo"))