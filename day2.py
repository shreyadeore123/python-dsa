#q1
# class student:
#     rollno=101

#     def msg(self): #Member function 
#         print("Hello World")

# obj = student() #object creation
# print(obj.rollno) #accessing data member
# obj.msg() #calling member 
# print(obj)

#q2
# class Demo:
#     def __init__(self):
#         print("I am constructor and i always called first")
    
#     #instance method
#     def info(self):
#         print("one object")

# obj = Demo()
# obj.info()
# obj2 = Demo()

#q3
# class Hod:
#     def __init__(self):#constructor
#         self.name='shreya deore'    #2 byte
#         self.age=21                 #3 byte
#         self.empid=1001             #1byte
#     def info(self):#instance method
#         print("My name is:",self.name)
#         print("My Age is:",self.age)
#         print("My Emp id is:",self.empid)  
# obj=Hod()#object creation
# obj.info()

# q4
# class Hod:
#     def __init__(self,name,age,rollno):#parameterized constructor
#         self.name=name    
#         self.age=age                 
#         self.rollno=rollno            
#     def info(self):#instance method
#         print('name=',self.name)
#         print('age',self.age)
#         print('rollno',self.rollno)
# obj=Hod('shreya deore',21,1001)#object creation
# obj.info()

# class New :
#     def __init__(self):
#      self.a = 10
   
# obj1 = New()
# obj2 = New()
# obj3 = New()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# class New:
#     a=10

#     def __init__(self):
#         self.name="shreya"

# obj1= New()
# obj2= New()
# obj3= New()
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# class college:
#     collegename="modern college"
#     def __init__(self):
#         self.stidentname="shreya"

# principle=college()
# teacher=college()
# accountant=college()
# print("principle=",principle.collegename,"....",principle.stidentname)
# print("teacher=",teacher.collegename,"....",teacher.stidentname)
# print("accountant=",accountant.collegename,"....",accountant.stidentname)
# college.collegename="HBD" #second way to change class variable
# principle.stidentname="shreya deore"
# print("principle=",principle.collegename,"|",principle.stidentname)
# print("teacher=",teacher.collegename,"|",teacher.stidentname)
# print("accountant=",accountant.collegename,"|",accountant.stidentname)

# intance varaibles are unique to each instance of a class, while class variables are shared among all instances of the class. 
# Instance variables are defined within the constructor using self, while class variables are defined directly within the class.   
# class student:
#     def __init__(self):
#         self.s_name=input("enter your name")
#         self.s_rollno=101  #instance method

#     def getdata(self):
#        self.s_mb=9890517978
    
# obj=student()
# obj.getdata()
# obj.s_branch="IT"  #adding instance variable to obj
# del obj.s_rollno
# print(obj.__dict__)

#static method
# class student:
#     #by using class name we can access static method
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("your contact details are:",firstname,lastname)
        
#     @staticmethod
#     def contact_detail(mobile,rollno):
#         print("your contact details are:",mobile,rollno)

# student.get_personal_detail("shreya","deore")
# student.contact_detail(9890517978,11)

#inheritance
#single level inheritance
# class college:
#     def college_name(self): #member fuction of college
#         print("college name is modern college")
# class student(college):#child class
#     def student_info(self):  #member function of student
#         print("Name:shreya deore")
#         print("branch:IT")
# obj=student()#obj create by class
# obj.college_name()
# obj.student_info()

#multilevel inhertance
# class college:
#     def college_name(self): 
#         print("college name is modern college")
# class student(college):#second class second-level
#     def student_info(self):  #member function of student
#         print("Name:shreya deore")
#         print("branch:IT")
# class Exam(student):#child class
#     def subject(self):  #member function of student
#         print("subject1:Design Engineering")
#         print("subject2:math")
#         print("C-language")
# obj=Exam()#obj create by class  
# obj.college_name()
# obj.student_info() 
# obj.subject()

# multiple inheritance
# class subjMarks:
#     math=int(input("enter your math marks"))
#     DE=int(input("enter your DE marks"))
#     C=int(input("enter your C marks"))
#     english=int(input("enter your english marks"))
#                        #parent class1
# class Practmath:
#     cpract=int(input("enter your practical marks"))
#                         #parent class2
# class Result(subjMarks,Practmath):#child class
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.C>=40 and self.english>=40 and self.cpract>=20:
#            print("pass")
#         else:
#            print("fail")
# obj=Result()
# obj.total()

#abstraction method
# from abc import ABC,abstractmethod
# class help4code(ABC):#abstractclass
#     @abstractmethod #decorator
#     def traning(self): #abstract method
#         pass

#     def placement(self):#abstractclass
#        pass

# class shreya(help4code):#SLH
#     def traning(self):
#         print('c,c++,java')
#     def placement(self):
#         print("java placement")

# class harsh(help4code):
#     def traning(self):
#         print('python|Django')
#     def placement(self):
#         print("python placement student")

# class riya(help4code):
#     def traning(self):
#         print('web development')
#     def placement(self):
#         print("web development placement")

# obj1=shreya()
# obj1.traning()
# obj1.placement()

# obj1=harsh()
# obj1.traning()
# obj1.placement()

# obj1=riya()
# obj1.traning()
# obj1.placement()


# from abc import ABC,abstractmethod
# class Ircts(ABC):#abstractclass
#     @abstractmethod #decorator
#     def bookTicket(self): #abstract method
#         pass

# class makemytrip(Ircts):#SLH
#     def bookTiket(self):
#         print("============================================================")
#         print("welcome to makemytrip.com")
#         self.source=input("Enter a sourc station name")
#         self.destination=input("Enter destniation name")
#         self.date=input("Enter date")
#         print("=======================================")

# class goibo(Ircts):
#     def bookTiket(self):
#         print("welcome")

# obj1=makemytrip()
# obj1.bookTiket()

# obj1=goibo()
# obj1.bookTiket()

#polymorphism
# class Arithmatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b,c):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# obj = Arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

# class Arithmatic:
#     def _init_(self,a):
#         print("there is no argument")
#     def _init_(self,a,b):
#         print("passing one argument")
#     def _init_(self,a,b,c):
#         print("passing two argument")

# obj = Arithmatic()
# obj.Arithmatic(10)
# obj.Arithmatic(10,20)/

# class Rbi:
#     def homeloan(self):
#         print("home loan rate of interest 8%")

#     def carloan(self):
#         print("car loan rate of interest 7%")

# class sbi(Rbi):#childclass 
#     def homeloan(self):
#         print("home laon rate of interest 10.5%")

# sbiobj = sbi()
# sbiobj.homeloan()
# sbiobj.carloan()

# class father:
#     def __init__(self):
#         print("father:= i am on time at breakfast table")

# class child(father):
#     def __init__(self):
#         #super().__init__():
#         print("child:= i will be late for brakfast")

# obj=child()


# #encapsulation
# class Base:#parent class
#     def __init__(self):
#         print("parent class constructor called")
#         self.a ="shreya"
#         self.__c ="harsh"
# #creating a derived class/child class
# class Derived(Base):#chid class
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         print("calling private member of base class:")
#         # print(self.a)
#         # print(self.__c)
# # obj1 =Derived()
# # print(obj1.a)
# # print(obj1._c)
# obj2 =Base()
# print(obj2.a)#accessible                                   
# print(obj2.__c)#not accessible



# class Base:#parent class
#     def __init__(self):
#         print("parent class constructor called")
#         self.a ="shreya"
#         self._c ="harsh"
# #creating a derived class/child class
# class Derived(Base):#chid class
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         print("calling private member of base class:")
#         # print(self.a)
#         # print(self._c)
# # obj1 =Derived()
# # print(obj1.a)
# # print(obj1._c)
# obj2 =Base()
# print(obj2.a)#accessible                                    #_single underscroll is protected
# print(obj2._c)#not accessible



#methods
# class Rbi:
#     def publicPolicy(self):
#         print("check the public policy of RBI")

#     def __privatePolicy(self):
#         print("thrre is some private policy which is not accessible public")

# class sbi:
#     def __init__(self):
#         Rbi.__init__(self)

#     def callingPublicmethod(self):  #child class public method
#         print("\nInside child class")
#         self.publicPolicy()      #calling paraent class public method

#     def callingPrivatemethod(self):#child class private method
#         self.__privatePolicy()#calling paraent class private method

# obj1 =sbi()
# obj1.callingPublicmethod()
# obj1.callingPrivatemethod()
# obj1.publicPolicy()
# obj1.__privatePolicy
# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
        
#from engineering.first_year.first_sem import f2_sem
#from Engineering.MCA.first_sem import first_subj
#from engineering.MCA.second_sem import second_subj
# importing modules from packages like subject name
choice =0 # global variable
class Exam(object):
    def __init__(self):
        self.sname=None
        self.collegename=0
        self.classname = 0
        self.rollno =0
        self.login()# calling function
        
    def login(self):# constructor part (called function)
            print("=========================")

            username=input("Enter username")
            password=input("Enter password")

            print("=========================")
            print()
            # Login section
            if username==password:
                print("Login successfully")
                self.getdata() # calling function
            else:
                print("Login fail try again")
 #=============================================================
    print()
    #Enter Your Profile Detail
    def getdata(self):
        self.sname      = input("Enter Your Name")
        self.collegename= input("Enter Your College Name")
        self.classname  = input("Enter Your Class Name")
        self.rollno     = input("Enter Your Roll Number")
        print()
        #====================End Of Profile Section========================
        # static subject declartion
        print(" choose any branch for giving exam")
        print("1. Mechanical Egineering")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Civil Engineering")
        print()

        choice = int(input("Enter your choice")) # subject selection logic part
        if choice==1:
            self.mechanical() # calling function
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        else:
            print("you have entered wrong choice")

        # called function part
    def mechanical(self):
        print("1. First Semester")
        print("2. Second Semester")
        print("Enter your Semester Number")
        # logical part
        choice =int(input("Enter your choice"))
        if choice == 1:
            #first_subj()  # calling function
            print("Math")
        elif choice== 2:
            pass #second_subj()

    def information(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice =int(input("Enter your choice"))
        if choice == 1:
            pass
        elif choice== 2:
            pass

    def computer(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice =input("Enter your choice")
        if choice == 1:
            pass
        elif choice== 2:
            pass

    def civil(self):
        print("1. First Semister")
        print("2. Second Semister")
        choice =input("Enter your choice")
        if choice == 1:
            pass
        elif choice== 2:
            pass

#object creation of class
#obj = Exam()
#obj.login()
#==================================================end=========================
# Examination Calculation part
class Calculation(object):
    def __init__(self):
        self.stat=0
        self.dmgt=0
        self.cg =0
        self.toc =0
        self.math=0
        self.total=0
        self.percentage=0
        self.ps = 0
        print()
        print("Do You Want To Put Examination Marks Enter Yes/No")
        print()
        Yes = input("Enter yes/no")
        if Yes == "yes":
            self.calculatemarks() # calling function
        else:
            print("Thank You For Visiting Here")
        print()
# taking a marks for subject
    def calculatemarks(self):                 
        self.stat = int(input("Enter Marks Of Statistics:"))
        self.dmgt = int(input("Enter Marks Of DMGT :"))
        self.cg   = int(input("Enter Marks Of CG   :"))
        self.toc  = int(input("Enter Marks Of TOC  :"))
        self.math = int(input("Enter Marks Of Math1:"))
        print()

        if self.stat >=40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
            self.ps="pass"
            print("You are pass")
        else:
            self.ps="Fail"
            print("You are fail")
            
        self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
        self.percentage = self.total/5.0


#obj1 = Calculation()    
#================================================================================

#Assesment class

class Assesment(Exam, Calculation): # multiple inheritance

    def __init__(self):    # child class constructor
        Exam.__init__(self)     # calling parent class constructor
        Calculation.__init__(self)

    def result(self):
        
        print("===============================================================")
        print("                                                               ")
        print("         College Name: ",self.collegename ,"                   ")
        print("                                                               ")
        print("===============================================================")

        print("|        Student Name: ",self.sname,  "                       |")
        print("|        Class Name  : ",self.classname,"                     |")
        print("|        Roll No     : ",self.rollno,      "                  |")
        print("===============================================================")
        print("                                                               ")
        print(" Subject Name     :     Total Marks    :  Obtained Marks :     ")                
        print("                                                               ")
        print(" Statistic        :",   "   100   "   "      :",  self.stat,  ":")
        print(" DMGT             :",   "   100   "   "      :",  self.dmgt,  ":")
        print(" CG               :",   "   100   "   "      :",  self.cg,    ":")
        print(" TOC              :",   "   100   "   "      :",  self.toc,   ":")
        print(" Math             :",   "   100   "   "      :",  self.math , ":")
        print("===============================================================")
        print("                                                               ")
        print("Result Status     :",                              self.ps,"   ")
        print("Total Marks       :",      "500",                           "  ")
        print("Obtained Marks    :",                          self.total,      )
        print("Percentage        :",      self.percentage,               "    ")
        print("===============================================================")

obj2 = Assesment()
obj2.result()