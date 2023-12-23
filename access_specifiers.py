class Student:
    def __init__(self, name, rollNo, age):
        self.name = name    #public insatnce var iable
        self._rollNo = rollNo  #Protected instance variable
        self.__age = age
    def __display(self):
        print(f"Hi my name is {self.name}, my roll number is {self._rollNo} and i am {self.__age} years old")
    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My roll no is {self._rollNo}")

s1 = Student("Dave", 24, 34)
print(s1._Student__age) # Name Mangling process using dir()
s1._Student__display()
# s1.displayPrivateData()
# s1.__display()



# b1 = Branch("Seoul", 22, 23)
# b1.display()
# b1.show()

