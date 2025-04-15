class Student:

    def __init__(self, name):
        self.name = name
        print("생성자 호출")

    def printInfo(self):
        print("학생정보 출력")
        print(f"이름: {self.name}")

    @staticmethod
    def printId():
        print("아이디 출력")

    def __str__(self):
        return f"이름: {self.name}"

s1 = Student("권민창")
print(s1)
s1.printInfo()
Student.printId()
