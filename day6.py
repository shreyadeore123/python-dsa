#positional argument
# def msg(val1,val2):
#     print("value 1=",val1)
#     print("value 2=",val2)
#calling function
# msg("admin","help4code")

#Keyword argument
# def msg(val1,val2):
#     print("value 1=",val1)
#     print("value 2=",val2)
#calling function
# msg(val1="admin",val2="help4code")

#default argument
# def city(cityname="nagpur"):
#     print("city name=",cityname)
# city("mumbai")
# city("nashik")
# city()

#variable length argument/variable number of argument
# def cityname(*city):
#     print(city)

# cityname("nashik","nagpur","pune","delhi","kalwan") 

# def arthimatic(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div #return multiple values at a same time in a python
# print(arthimatic(5,5))

#nested loop
# for i in range(1,4):#outer loop represent row
#     for j in range(1,4):#inner loop represent column
#         print(i,end=" ")
#     print()

# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()


# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()



# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#         print("*"*i)



# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()

# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+i):
#         print(chr(64+i),end=" ")
#     print()

# import time
# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(2)
#         print(n+1-i,end=" ")
#     print()

# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+n-i),end=" ")
#     print()

# import time
# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+i):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

# import re
# count=0
# pattern=re.compile("function")
# print(pattern)
# matcher=pattern.finditer(" a function in python id define by a def statement.python the general syntax look like this: def function-name(parameter list): statement,i.e. the function  body.the parameter python list consist of none or more parameter.")
# print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"....",i.group())
#     print("the number of occurrences:",count)


# import re
# count=0
# # pattern=re.compile("function")
# # print(pattern)
# matcher=re.finditer("hi","hihihihi")
# print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"....",i.group())
#     print("the number of occurrences:",count)

# import re
# obj=input("enter any character:")
# objmatch=re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"....",match.group())

# import re
# a=input("enter string to perform match operation:")
# match=re.match(a,"python is very imp language")
# print(match)
# if match!=None:
#     print("match found at begining level")
#     print(match.start()," ",match.end())
# else:
#     print("there is no matching at begining level")


# import re
# a=input("enter string to perform match operation:")
# match=re.fullmatchmatch(a,"pythonisvery")
# print(match)
# if match!=None:
#     print("match found ")
#     print(match.start()," ",match.end())
# else:
#     print("full match not found")


# import re
# a=input("enter string to perform match operation:")
# match=re.fullmatchmatch(a,"python sss dynamic lannn")
# print(match)
# if match!=None:
#     print(match.start()," ",match.end(),"",match.group())
# else:
#     print("there is no matching anywhere")



# import re
# match=re.findall('[^0-9a-zA-Z]',"abch3h5bk7ZQ$&")
# print(match)

# import re
# obj=re.sub('[a-b]','X','1234 ABCD dhhh')
# print(obj)

# import re
# obj=re.subn('[0-7]','@','hbdhdhjddhhh')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement is=","obj[1]")

#wapp to check whether the given mail
#valid gmail id or not
# import re   
# s=input("enter mail id:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@sitrc[.]org",s)                                                               
# if m!=None:
#     print("valid email id")
# else:
#     print("invalid email id")


# import re   
# mo=input("enter mobile no:")
# m=re.fullmatch("[0-9]\d{9}",mo)                                                               
# if m!=None:
#     print("valid mobile")
# else:
#     print("invalid mobile no")


# import re
# a=input("enter string performance match operation")
# f=open('shreya.txt','r')
# c=f.read()
# match =re.search(a,c)
# print(match)
# if match!=None:
#     print("match found at begining level")
#     print(match.start,"",match.end())
# else:
#     print("there is no matching at begining level")


# when the main problem can be able to divide into similar sub problem then we use recursion
#factorial solution
# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))


# def isPalindrone(str):
#     if len(str)==0:
#         return True
#     if str[0]!=str[len(str)-1]:
#         return False
#     return isPalindrone(str[1:-1])

# print(isPalindrone('awesone'))
# print(isPalindrone('foobar'))
# print(isPalindrone('tacocat'))
# print(isPalindrone('bshhbhbhbcjhjhs'))

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))


def productofarray(arr):
    if len(arr)==0:
        return 1
    return arr[0]*productofarray(arr[1:])

print(productofarray([1,2,3]))
print(productofarray([1,2,3,4,10]))