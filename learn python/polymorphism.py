# class Greet:
#     # def display(self):
#     #     print("good morning")
        
#     # def display(self, firstname=""):
#     #     print("good morning :" ,firstname)
        
#     def display(self, firstname="",lastname=""):
#         print("good morning :", firstname , lastname)
# # a=input("enter your name")     
# obj=Greet()
# obj.display()
# obj.display("vipin")
# obj.display("vipin","kushwaha")

#################################

class rectrangeler:
    def __init__(self,L,W):
        self.L=L
        self.W=W
    def calculate_area(self):
        return self.L*self.L

class circle:
    def __init__(self,r):
        self.r = r
    def calculate_area(self):    
        return 3.14*self.r*self.r

def area(shape):
    shape.calculate_area()
    
user_value=float(input("enter your value :"))
user_value1=float(input("enter your value :"))

rec=rectrangeler(user_value,user_value1)
area(rec)
# result=rec.calculate_area()
# print(result)

cir=circle(user_value)
area(cir)
# res = cir.calculate_area()
# print(res)


    
# user_value=float(input("enter your value :"))
# obj1=circle(user_value)
# res = obj1.calculate_area()
# print(res)


