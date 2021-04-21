#n1,n2를 인자로 받아 더해주는 함수
def add_number(n1,n2):
    ret=n1+n2
    return ret

#t1,t2를 인자로 받아 더한 값만 보여주는 함수
def add_text(t1,t2):
    print(t1+t2)

#전역변수,지역변수
param=10
strdata="전역변수"

def func1():
    strdata="지역변수"
    print(strdata)

def func2(param):
    param=1

def func3():
    global param
    param=50

func1()         # 지역변수
print(strdata)  # 전역변수
                
print(param)    # 10
func2(param)     
print(param)    # 10

func3()       
print(param)    # 50
