# def calculator(n1,n2):
#     print("1. +")
#     print("2. -")
#     print("3. *")
#     print("4. /")
#     pick_num=int(input())
#     n1=int(input())
#     n2=int(input())
#     if pick_num==1: 
#         return n1+n2
#     if pick_num==2: 
#         return n1-n2
#     if pick_num==3: 
#         return n1*n2
#     if pick_num==4: 
#         return n1/n2

def calculator(arr,divisor):
    list1=[]
    for i in arr:
        if i%divisor==0:
             #요소 4개 
            list1.append(i)
    return list1