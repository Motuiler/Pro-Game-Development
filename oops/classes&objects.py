class Student():
    #Class Variables have the same value for all objects
    school='CJD'

    #Instance Variables have different values for different objects
    #Constructer
    def __init__(self,name,age,year):
        self.name=name
        self.age=age
        self.year=year

    def result(self,math,english,art,sport,physics):
        score=math+english+art+sport+physics
        average=score/5
        print(f'Your total score:{score}')
        print(f'Your average:{average}')

student1=Student('Ahorn',6,1)
print(student1.school)
print(student1.name)
print(student1.age)
print(student1.year)
student1.result(32,47,23,13,89)

student2=Student('Bob',15,6)
print(student2.school)
print(student2.name)
print(student2.age)
print(student2.year)
student2.result(99,99,87,100,91)