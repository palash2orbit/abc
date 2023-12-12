# for loop
# list= 'palash'
# for x in list:
#  print(x)

# a = 0
# aman = [35,70,80,45]
# for x in aman:
#     a = a+x
# a = a/4
# print(a)
# if (a>=33):
#     print('pass')
# else:
#     print('fail')

##########################
# while loop

# i = 0
# while i<10:
#     print(i)

# i=1
# while i<100:
#     if(i%2==1):
#         print(i)
#     i=i+1

############################

# i = 0
# for x in range(1,100):
#     if(x>=40):
#         print(x)

# i = 0
# while  i<101:
#     if(i>=40):
#         print(i)
#     i =i+1
##############################33
# for i in range(1,11):
#     print("2" ,"x" ,i,"=",2*i)

#################################
# my_list = [2,4,6,8,10,12,14,15,16]
# for i in my_list:
#  print(i)
#################################
# my_str ="python"
# for i in my_str:
#     print(i)
    
###########################
# my_set = {1,2,3,4,3.14,'hello',3+4j,4,5}
# for i in my_set:
#     print(i)
################################
# my_dict ={
#     'name':'inocrypt',
#     'address':'napiar town',
#     'mobile number':'1254585485'}
# for i,z in my_dict.items():
#      print(i,z)
#####################################

# my_dict ={
#     'name':'inocrypt',
#     'address':'napiar town',
#     'mobile number':'1254585485'}
# for z in my_dict.values():
#      print(z)
########################################
# for i in range(1,3):
#     for j in range(1,3):
#         print('j')

############################################

# for i in range(0,3):
#     for j in range(2,4):
#         # for z in range(0,4):
#           print(i)
#############################
# for i in range(0,3):
#     for j in range(0,3):
#           print(j)
#############################
# for i in range(0,5):
#     for j in range(0,4):
#           print('*')
################################3

# for i in range(1,4):
#     for j in range(0,4):
#         for k in range(1,3):
#           print(k)
###################################
# # pass
# for i in range(1,5):
#   pass

# def add(a,b):
#   pass

# for i in range (1,11):
#   if i==5:
#    print(i)
#   break

# for j in range (1,11):
#   print(j)
#   if j==5:
#     break

# for j in range (1,11):
#   if j==5:
#     continue
#   print(j)

# for j in range (1,11):
#   if j==5:
#     pass
#   print(j)
##################################

# for i in range(1,6):
#   for j in range(1,i+1):
#       print('*',end='')
#   print()

############################
# a =1
# while a<10:
#   print(a)


# password = 'ino*123'
# user_pwd = input('enter your pass word:')
# while password == user_pwd:
#   if password == user_pwd:
#      print('success')
#      break
# else:
#  print('wrong pwd')
###########################################

password = 'ino*123'
pwd_count = 0
while pwd_count<3:
  pwd_count = pwd_count+1
  user_input = input('enter your password:')
  if (user_input==password):
    print('success')
  else:
    print('try again')