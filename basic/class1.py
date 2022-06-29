# 학생 3명의 정보

# 변수

# 학생1
# student_name1 = "Kim"
# student_number_1 = 1
# student_grade_1 = 1
# student_detail_1 = [{"gender": "male"}, {"score1": 97}, {"score2": 88}]

# 학생2
# student_name2 = "Park"
# student_number_2 = 2
# student_grade_2 = 2
# student_detail_2 = [{"gender": "female"}, {"score1": 87}, {"score2": 96}]

# 학생3
# student_name3 = "Choi"
# student_number_3 = 3
# student_grade_3 = 3
# student_detail_3 = [{"gender": "male"}, {"score1": 66}, {"score2": 78}]


# 클래스
class Student:  # 괄호는 필수 아님
    # __init__ : 생성자, self : this와 같은 개념
    def __init__(self, name, number, grade, details):
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    # toString 개념
    def __str__(self):
        return "name : {}, number : {}, grade : {}, details : {}".format(
            self.name, self.number, self.grade, self.details
        )


# 객체생성
student1 = Student("Kim", 1, 1, {"gender": "male", "score1": 97, "score2": 88})
student2 = Student("Park", 2, 2, {"gender": "female", "score1": 87, "score2": 96})
student3 = Student("Choi", 3, 3, {"gender": "male", "score1": 66, "score2": 78})

print(student1)  # <__main__.Student object at ........ >
print(student2)
print(student3)

# class Student{
# private String name;
# private int number;
# public Student(String anme, int number ....){
#   this.name = name;
# }
# public String toString(){
#   return "name:"+name.....
# }
# }
# self를 붙여서 하면됨.
