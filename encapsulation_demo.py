class Student:
    def __init__(self, name, rollNo, age):
        self.name = name    #public insatnce var iable
        self._rollNo = rollNo  #Protected instance variable
        self.__age = age
    
    def get_age(self):
        try:
            if self.__age > 35:
                return ("Invalid age given")
            else:
                return self.__age
        except:
            return ("Invalid error")
 
    def set_age(self,age):
        if age > 35:
            print("Invalid age given... Age should be less tan 35")
        else:
            self.__age = age 

#     def __display(self):
#         print(f"Hi my name is {self.name}, my roll number is {self._rollNo} and i am {self.__age} years old")
#     def displayPrivateData(self):
#         self.__display()

# class Branch(Student):
#     def show(self):
#         print(f"My roll no is {self._rollNo}")

s1 = Student("Dave", 24, 26)
print(s1.get_age())
s1.set_age(12)
print(s1.get_age())
#print(s1._Student__age) # Name Mangling process using dir()
#s1._Student__display()
