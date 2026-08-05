class Subject:
    def __init__(self, sub1, sub2, sub3, sub4, sub5):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5


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

        print("Student Report")
        print("--------------")
        for idx, (mark, grade) in enumerate(zip(marks, grades), start=1):
            print(f"Subject {idx}: {mark} => {grade}")
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
