
def Solve(Number):
    dnumber=Number
    d1number=0
    answer=0
    while Number>0:
        d1number=d1number+(Number%10)
        Number//=10
    answer=dnumber+d1number
    return answer

Number=1000
arr=[]
for i in range(1,Number+1):
    arr[Solve(i)]=1
    print(Solve(i))
for i in range(1,Number+1):
    if(arr[i]!=1):
        print(i)