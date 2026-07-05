# mydict = {
#     101:"shreya",
#     102:"harsh",
#     103:"anu",
#     104:"riyaa",
#     101:"sanika",
#     104:"sanika",
# }

# print(mydict)
# print(type(mydict))
# #with the help of key we have print values
# a= mydict[102]
# print(a)

#we will replace old value by new value
# mydict[102]="harsh"
# print(mydict)

#only print key x=1,1
# for x in mydict:
#   print(x)

# we print value x=0
# for x in mydict.values():
#   print(x)

#printing key and values both
# for x,y in mydict.items():
#   print(x,y)

#if i have to add new key and value pair in my dictonary
# mydict["mobile_no"]=9960734229
# print(mydict)


# mydict={
#     101:"shreya",
#     "professional":"developer",
#     "empid":1120
# }
# mydict.pop(101)
# print(mydict)
#pop() method remove pair by spsecific key name



# mydict={
#     101:"shreya",
#     "professional":"developer",
#     "empid":1001
# }
# mydict=mydict.copy()
# print(mydict)


#q1 write a function to check if a dictonary is empty
# mydict = {
#     'a':10,
#     'b':20,
#     'c':30,
#     'd':40
# }
# max_value=1
# for value in mydict.values():
#    if value>max_value:
#     max_value=value

#     print(max_value)

# mydict={}
# if mydict:
#   print("empty")
# else:
#   print("not empty")

#q2 write a function to reverce the key value pairs of a dictonary
# mydict={
#   "a":1,
#   "b":2,
#   "c":3
#  }
# rev={value:key for key,value in mydict.items()}
# print(rev)

#q3 find the common key value pair in 2 dictionary

# dict1:{"a":1,"b":2,"c":3}
# dict2:{ "B":2,"C":4,"D":5}
# common={}
# for key in dict1:
#     if key in dict2 and dict1[key]==dict2[key]:
#         common[key]=dict1[key]
#     print(common)


#linear search
# def linearsearch(array,target):
#     for i in range(len(array)):#i=0
#         if array[i]==target:
#             return i

# array=[1,2,3,4,5,6,7,8,9]
# target=7
# result=linearsearch(array,target)#calling function
# if result !=-1:
#     print("element found at index no=",result)
# else:
#     print("element not found")

#find the maximum and minimum value
arr=[5,3,9,2,8]
# min_val=arr[0]
# max_val=arr[0]
# for i in range(1,len(arr)):
#     if arr[i]<min_val:
#         min_val=arr[i]

# print("manimum:",min_val)
# print("maximum:",max_val)

#find the majority element
arr=[3,3,4,2,44,2,4,4]
# for i in arr:
#     count=0
#     for j in arr:
#         if i==j:
#             count +=1

#     if count>len(arr)//2:
#         print("majority element",i)
#     else:
#         print("no,majority element")

#file handiling
# Whenever we want to store data for future purpose so use a filehandling
# f=open("myfile.txt","w")
# print("name of file:",f.name)
# print("file mod e:",f.mode)
# print("readable:",f.readable())#method
# print("writable:",f.writable())
# print(" file closed:",f.closed)
# f.close
# print("file closed:",f.closed)

# f=open("myfile.txt", "w")
# f.write("\n pune is smart city")
# f.write("\n nashik is smart city")
# f.write("\n nagpur is smart city")
# f.write("\n banglore is smart city")
# f.write("\n kalwan is smart city")
# f.close
# print("file operation is done")

# f=open("newfile.txt", "w")
# mylist=["shreya","riya","anu"]
# f.writelines(mylist)
# f.close
# print("written work has done successfully")

# f=open("myfile.txt","r")
# print(f.read())
# f.close()

# with open("myfile.txt","w")as f:
#     f.write("shreya\n")
#     f.write("anu\n")
#     f.write("riya\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)

# with open("myfile.txt","r")as f:
#     content = f.read()
#     print(content)

# f1=open("wallpaper.jpg","rb")
# f2=open("rossom.jpg","wb")
# data=f1.read()
# f2.write(data)


#operation with csv file
# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)#here it will returb csvwriter object
# a.writerow(["student","rollno","name","mobileno"])

# studentid=int(input("enter student id:"))
# rollno=int(input("enter rollno:"))
# name=input("enter name:")
# mobileno=int(input("enter mobileno:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")

# import csv
# f=open("result.csv","a",newline="")
# a=csv.writer(f)
# a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])
            
# rollno=int(input("enter rollno:"))
# name=input("enter name:")
# mobileno=int(input("enter mobileno:"))
# p1=int(input("enter p1 marks:"))
# p2=int(input("enter p2 marks:"))
# p3=int(input("enter p3 marks:"))     
# email=(input("enter email:"))       
# if p1>40 and p2>=40 and p3>=40:
#     result="pass"
#     print("you are pass")
# else:
#     result="fail"
# total=p1+p2+p3
# percentage=total/3.0
# a.writerow([rollno,name,p1,p2,p3,total,percentage,email,result])           
# print("student record has save")        
            

import sys
class Queue:
    def __init__(self,queuesize):#parameter constructor
        self.queuesize=queuesize
        self.myQueue=[]

    def isfull(self):
         if len(self.myQueue) == self.queuesize:
           return True
         else:
            return False

    def isEmpty(self):
        if self.myQueue==[]:
            return True
        else:
            return False
   
    def enQueue(self,value):
        if self.isfull():
            print("Queue is full")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.myQueue ==[]:
            print("queue is empty")
        else:
            print(self.myQueue)

    def deQueue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print(self.myQueue.pop(0))

    def frontpeek(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            print(self.myQueue[0])

    def deletequeue(self):
        self.myQueue=None
2


size=int(input("enter the sizeof Queue:"))
queObj=Queue(size)        
while True:
    print("1.enQueue")
    print("2.display")
    print("3.deQueue")
    print("4.frontpeek")
    print("5.DeleteQueue")
    print("6.Exit")
    choice=int(input("enter your choice: "))
    if choice ==1:
        value=int(input("enter value to add in queue:"))
        queObj.enQueue(value)
    elif choice ==2:
        queObj.display()
    elif choice ==3:
        queObj.deQueue()
    elif choice ==4:
        queObj.frontpeek()
    elif choice ==5:
        queObj.deletequeue()
    elif choice ==6:
        sys.exit()
    
    
    