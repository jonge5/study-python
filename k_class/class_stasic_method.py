class Student:
    status = '쉬는 중'  # static 변수

    def __init__(self, kor, eng, meth):
        self.kor = kor
        self.eng = eng
        self.method = meth

    @staticmethod
    def print_start_time_of_study():
        print('9시 떙')
        Student.status = '공부 중'



han = Student(0, 0, 0)
hong = Student(0, 0, 0)
print(Student.status)

Student.print_start_time_of_study()
print(Student.status)

