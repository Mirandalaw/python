class MyClass:
    #클래스 맴버
    var='hello'

    def say_hello(self):
        #지역변수
        param1="world" 
        print(param1)
        #클래스 맴버 출력
        print(self.var)
        #인스턴스 맴버
        self.instance="I am instance member"

obj=MyClass()
print(obj.var)
obj.say_hello()
print(obj.instance)
# Class 멤버 : 클래스 메소드 밖에서 선언되는 변수
# Instance 멤버 : 클래스 메소드 안에서 self와 함께 선언되는 변수