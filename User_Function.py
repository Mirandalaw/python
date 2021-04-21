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

x=1
y=2
z=3

#받은 인자를 뒤집어 주는 함수
def reverse(x,y,z):
    return z,y,x

#실행 부분 정수형
ret=reverse(x,y,z)
print(ret)

#실행부분 tuple형
tupledata=reverse('a','b','c')
print(tupledata)

r1,r2,r3=reverse('a','b','c')
print(r1,r2,r3)

r4=reverse('a','b','c')
print(r4)

def Solve_Number1(Number):
    behind_str="*******"
    Behind_Phone_Number=(behind_str[0:]+Number[7:])
    return Behind_Phone_Number

# Phone_Number=input("")
# B_P_N=Solve_Number1(Phone_Number)
# print(B_P_N)
#
# Alphabet=input("")
# The_Number=len(Alphabet)
# last_Number=The_Number%5
# mok=The_Number//5
# i=0
# while(i!=mok):
#     print(Alphabet[(0+i*5):5+(i*5)])
#     i=i+1
# print(Alphabet[(5*mok):(5*mok+last_Number)])

def F(n):
    if n==1 :
        return 1
    if n==0 :
        return 0
    if n>1:
        return F(n-1)+F(n-2)

# Input_Num=int(input(""))
# F(Input_Num)
the_number=list(input(""))
the_number.sort(reverse=True)
l=len(the_number)
answer= l-2
print(the_number[0:answer])
