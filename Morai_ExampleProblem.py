#소수의 개수 구하기

def is_prime_number(Get_Num):
    if Get_Num==2:
        return True
    elif Get_Num<2:
        return False
    else:
        for i in range(2,Get_Num):
            if (Get_Num%i)==0:
                return False
            return True


Get_Num=int(input(""))
cnt=0
for i in range(2,Get_Num+1):
    print(is_prime_number(i))
    if is_prime_number(i)==True :
        cnt=cnt+1
print(cnt)