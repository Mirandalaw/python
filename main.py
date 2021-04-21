sum=0
Scorelist = []
while True:
    Get_Score = int(input(""))

    Scorelist.append(Get_Score)
    print(Get_Score)
    if Get_Score>=90 :
        print("A")
    elif Get_Score>=80 and Get_Score<=89:
        print("B")
    elif Get_Score>=70 and Get_Score<=79:
        print("C")
    elif Get_Score>=60 and Get_Score<=69:
        print("D")
    else :
        print("F")
    if(Get_Score==0):
        for i in range(0,len(Scorelist)):
            sum+=Scorelist[i]
        print(sum/len(Scorelist))
        break