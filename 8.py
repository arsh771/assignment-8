#Q1
class circle:
    def __init__ (self,r):
        self.radius=r
    def getArea(self):
        self.area=3.14*self.radius*self.radius
        return self.area
    def getCircumference(self):
        self.c=2*3.14*self.radius
        return self.c
r=int(input("Enter radius of circle "))
c1=circle(r)
print("Area of circle is:",c1.getArea())
print("Circumference of circle is:", c1.getCircumference())

#Q2
class student:
    def __init__(self,name,rno):
        self.name=name
        self.rollno=rno
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No.:",self.rollno)
        print("Age:",self.age)
        print("Marks:",self.marks)
name=input("Enter name: ")
rno=int(input("Enter rollno: "))
age=int(input("Enter the age of student "))
marks=int(input("Enter marks of student "))
s1=student(name,rno)
