# class MyClass:
#     #클래스 맴버
#     var='hello'

#     def say_hello(self):
#         #지역변수
#         param1="world" 
#         print(param1)
#         #클래스 맴버 출력
#         print(self.var)
#         #인스턴스 맴버
#         self.instance="I am instance member"

# obj=MyClass()
# print(obj.var)
# obj.say_hello()
# print(obj.instance)
# # Class 멤버 : 클래스 메소드 밖에서 선언되는 변수
# # Instance 멤버 : 클래스 메소드 안에서 self와 함께 선언되는 변수


#N명의 학생 이름, 학번, 성적을 입력받고  각 학생의 평균 구하기
class student:
    def __init__(self,name,number,sub1,sub2,sub3):
        self.name=name
        self.number=number
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def average(self):
       
        self.Sum=self.sub1+self.sub2+self.sub3
        self.Aver=self.Sum/3
    
    def student_info(self):
        print("학생의 이름 : {}",format(self.name))
        print("학생의 학번 : {}",format(self.number))
        print("학생의 과목1 : {}",format(self.sub1))
        print("학생의 과목2 : {}",format(self.sub2))
        print("학생의 과목3 : {}",format(self.sub3))
        print("학생의 평균 : {}",format(self.Aver))
       
obj=[]

name_list=[]
number_list=[]
sub1_list=[]
sub2_list=[]
sub3_list=[]
for i in range(0,1):    
    name = input("{0}번쨰 학생의 이름 >>".format(i))
    number = input("{0}번쨰 학생의 학번 >>".format(i))
    sub1 = int(input("{0}번쨰 학생의 과목1 >>".format(i)))
    sub2 = int(input("{0}번쨰 학생의 과목2 >>".format(i)))
    sub3 = int(input("{0}번쨰 학생의 과목3 >>".format(i)))
    name_list.append(name)
    number_list.append(number)
    sub1_list.append(sub1)
    sub2_list.append(sub2)
    sub3_list.append(sub3)

s1 = student(name_list[0],number_list[0],sub1_list[0],sub2_list[0],sub3_list[0])
# s2 = student(name_list[1],number_list[1],sub1_list[1],sub2_list[1],sub3_list[1])
# s3 = student(name_list[2],number_list[2],sub1_list[2],sub2_list[2],sub3_list[2])
s1.average()
s1.student_info()
# s2.average()
# s2.student_info()
# s3.average()
# s3.student_info()
    


