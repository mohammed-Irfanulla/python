#class creation
# class car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
# car1=car("xyz",123,2006)
# print(car1.year,car1.model)

#book class
# class book:
#     def __init__(self,bid,author,title,price):
#         self.bid=bid
#         self.author = author
#         self.title = title
#         self.price=price

# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)
# print(dog1.name) 
# print(dog1.species)
# dog2 = Dog("Bulldog", 1)
# print(dog2.name) 
# print(dog2.species)
# print(dog1,dog2)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         pass
# class student(person):
#     def __init__(self,name,age,roll_no,marks):
#         super().__init__(name,age)
#         pass

# class employee(person):
#     def __init__(self, name, age,exp,sal):
#         super().__init__(name, age)
#         self.exp=exp
#         self.sal=sal
# employee1=employee("irfan",20,2,20000)
# print(employee1.name,employee1.sal)

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal):
#     def sound(self):
#         print(self.name, "barks")

# class Cat(Animal):
#     def sound(self):
#         print(self.name, "meow")

# d = Dog("Buddy")
# # Inherited method
# d.info()     
# d.sound()
# d2=Cat("cat")
# d2.info()
# d2.sound()

# # Parent Class: Animal
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# # Child Class: Dog
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Calls constructor based on MRO
#         super().__init__(name)  #you can initialize parent class attributes through child class also!
#         self.breed = breed

#     def details(self):
#         print(self.name, "is a", self.breed)

# d = Dog("Buddy", "Golden Retriever")
# #d.info()      # Parent method, which can also skipped!
# d.details()   # Child method

# class father:
#     def __init__(self,fname,fage):
#         self.fname=fname
#         self.fage=fage
# class mother:
#     def __init__(self,mname,mage):
#         self.mname=mname
#         self.mage=mage
# class child(father,mother):
#     def __init__(self, fname, fage,mname,mage,name,age):
#         father.__init__(self,fname,fage)
#         mother.__init__(self,mname,mage)
#         self.name=name
#         self.age=age
#     def info(self):
#         print(self.fname,self.mname,self.name)
# child1=child("raj",12,"raji",12,"rajesh",10)
# child1.info()

'''class employee with name salary craete another class devoloper that inheritsb the property of employe  and
 again create another calss hr that will inherite the calss employee and devoloper'''

# class employee:
#     def __init__(self,eid,ename,eage):
#         self.eid=eid
#         self.ename=ename
#         self.eage=eage
# class dev(employee):
#     def __init__(self,did,dname,dexp):
#             self.did=did
#             self.dname=dname
#             self.dexp=dexp
# class hr(dev,employee):
#      def __init__(self, eid, ename, eage,did,dname,dexp,hrname,hrage):
#           employee.__init__(self,eid,ename,eage)
#           dev.__init__(self,did,dname,dexp)
#           self.hrname=hrname
#           self.hraage=hrage
#      def info(self):
#           print(f"Emp_name:{self.ename},dev_name:{self.dname},HR_name:{self.hrname}")
# ename=input("emp name:")
# eid=int(input("eid:"))
# eage=int(input("eage:"))
# did=int(input("did:"))
# dname=input("dev name:")
# dexp=int(input("did:"))
# hrname=input("hr name:")
# hrage=int(input("hr_age:"))
# hr1=hr(eid,ename,eage,did,dname,dexp,hrname,hrage)
# hr1.info()

'''hybrid inheritance'''
# class a:
#     def prnta(self):
#      print("im from a")
# class b(a):
#     def prntb(self):
#        print("im from b")
# class c:
#    def prntc(self):
#       print("im from c")
# class d(b,c):
#    def prntd(self):
#       print("im from d")
# d1 = d()
# d1.prnta()
# d1.prntb()
# d1.prntc()
# d1.prntd()

'''Student grade management'''

class Subject:
    def __init__(self, sub1, sub2, sub3, sub4, sub5):
        self.sub1 = sub1
        self.sub2 = (sub2)
        self.sub3 = (sub3)
        self.sub4 = (sub4)
        self.sub5 = (sub5)

class GradeCal:
      @staticmethod
      def mark(marks):
         if marks > 90:
               return "O"
         elif 80 <= marks <= 90:
               return "A+"
         elif 70 <= marks < 80:
               return "B+"
         elif 60 <= marks < 70:
               return "B"
         elif 30 <= marks < 60:
               return "C"
         else:
               return "F"


class Report(Subject, GradeCal):
    def __init__(self, sub1, sub2, sub3, sub4, sub5):
        super().__init__(sub1, sub2, sub3, sub4, sub5)

    def report(self):
        marks = [self.sub1, self.sub2, self.sub3, self.sub4, self.sub5]
        grades = [self.mark(mark) for mark in marks]
        total = sum(marks)
        average = total / len(marks)
        overall_grade = self.mark(average)

        report_lines = [
            ("Subject 1", self.sub1, grades[0]),
            ("Subject 2", self.sub2, grades[1]),
            ("Subject 3", self.sub3, grades[2]),
            ("Subject 4", self.sub4, grades[3]),
            ("Subject 5", self.sub5, grades[4]),
        ]

        print("Student Report")
        print("--------------")
        for subject_name, mark, grade in report_lines:
            print(f"{subject_name}: {mark} => {grade}")
        print("--------------")
        print(f"Total Marks : {total}")
        print(f"Average     : {average:.2f}")
        print(f"Overall     : {overall_grade}")


class Student(Report):
    def __init__(self, usn, sname, sclass, ssec, dob, sub1, sub2, sub3, sub4, sub5):
        super().__init__(sub1, sub2, sub3, sub4, sub5)
        self.usn = usn
        self.sname = sname
        self.sclass = sclass
        self.ssec = ssec
        self.dob = dob

    def print_report(self):
        print(f"USN    : {self.usn}")
        print(f"Name   : {self.sname}")
        print(f"Class  : {self.sclass}")
        print(f"Section: {self.ssec}")
        print(f"DOB    : {self.dob}")
        print()
        super().report()


if __name__ == "__main__":
    student = Student(
        usn="1RV17IS001",
        sname="Irfan",
        sclass="4th",
        ssec="A",
        dob="2004-01-01",
        sub1=92,
        sub2=85,
        sub3=77,
        sub4=66,
        sub5=53,
    )
    student.print_report()

