# var=[7,3,9,2,8]
# var.sort()
# print(var[-2])

# num=input().strip()
# freq=[0]*10
# for digit in num:
#     freq [int (digit)]-1

# q1
# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# q2
# a=[1,2,3,4,5,6,7,8,9,10,]
# a[::2]=10,20,30,40,50,60
# print(a)

# q3
# a=[1,2,3,4,5]
# print(a[3:0:-1])

# q4
# def func(value,values):
#      var=1                                            
#     values[0]= 44
# t=3
# v=[1,2,3]                              
# func(t,v)
# print(t,v[0])

# q5
# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],             
#      [12,13,14,15]]
# for i in range(0,4):#i=0
#     print (arr[i].pop())

# q6
# def f(i,value=[]):
    # value.append(i)   [1][1,2][1,2,3]
#     print(value)
#     # return value
# f(1)
# f(2)
# f(3)

# q7
# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print (arr[i],end="")

# q8
# fruit_list1 =['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] ='Guava'
# fruit_list3[1 ]= 'kiwi'

# sum=0
# for ls in(fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] =='Kiwi':
#         sum +=20
#         print(sum)
                                                                                               #   q depend on list allizing



# q9
# for i,j in zip (range(1,6),range(5,0,-1)):
#     if i ==3 and j==3:
#         continue
#     print(i,"",j)

# q10
# # data=[[1,2][3,4],[5,6],[7,8]]
# def fun(m):
#     v= m[0][0]
#     for row in m:
#         for element in row:
#             if v < element: v=element
#             return v
#         print(fun(data[0]))

# init_tuple=()
# print(init_tuple.__len__())     default Value gives 0

# init_tuple_a='a','b'
# init_tuple_b('a','b')
# print(init_tuple_a == init_tuple_b)

# l=[1,2,3]
# init_tuple =('Python',)*(1.__len__() -1[::-1][0])
# print(init_tuple)

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[(4,5)])

# a={'a':1,'b':2,"c":3}
# print(a['a','b'])


# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index] +=1
#     else:
#         fruit[index] =1
# addone('Apple')                  uppercase
# addone('Banana')
# addone('apple')
# print(len(fruit))               lowercase

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# sum=0
# for k in arr:
#     sum+= arr[k]
# print(sum)

# my_dict ={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)


# my_dict ={}
# my_dict[1,2,4]=8
# my_dict[4,2,1]=10
# my_dict[1,2]=12
# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)
# print(my_dict)

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))  

# dict ={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# math=50
# chem=60
# print(id(math))
# print(id(chem))

# rec = {"Name":"Python","Age":20"}
# r= rec.copy()
#  print(id(r) == id(rec))

# rec = {"Name" : "Python", "Age":"20", "Addr" :"NJ", "Contry":"USA"}
# id1=id(rec)
# del rec
# rec = {"Name" : "Python","Age":"20","Addr" :"NJ","Contry":"USA"}
# id2=id(rec)
# print(id1==id2  )      

# val=input("Enter the value for vali:")
# val2=input("Enter the val2 value")
# print(val+val2)
# print(2+2)
# print("2"+"2")


# int()used to convert /..
# print(int(3.14))
# print(int(True))
# print(int(True))
# print(int(False))
# print(int("4"))

# print (float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))
      

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2))
# print(bool(0+0))


# problem soving
# move to zero to the End 
#   given an array,move all the zeros to the end without changing
# val=[0,1,0,3,12]
# for i in val:
#     if i == 0:
#         val.remove(i)
#         val.append(i)
# print(val)


# find the three intersection of 3 array
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in  B and i in C:
#         print(i)

# maximum consective once
# A =[1,1,0,1,1,1,0,1,1,1,1]
# count=0
# max_count=0
# for i in A:
#     if i ==1:
#         count +=1
#         if count > max_count:
#         max_count = count
#     else:
#         count=0
# print(max_count)

# check palindeomic list
# A=[1,2,3,2,1]
# if A[:]== A[::-1]:
#     print("palindeomic list")
# else:
#     print("not palindrome")

# reverse string
# name="Hello" 
# for i in name:
#     print(i)




# name="Hello" 
# N=len(name)-1
# newname=""
# for i in range(N,0,-1):
#     newname += name [i]
#     print(newname)

# remove duplicate from a string
# name="programming"
# newname=" "
# for i in name:
#     if i not in newname:
#         newname+=i
# print(newname)


