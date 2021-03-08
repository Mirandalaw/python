import random

numbers=[]
for num in range(0,10):
    numbers.append(random.randrange(0,10)) #append는 리스트에 뭔가를 더 추가함.

print("생성된 리스트",numbers)

for num in range(0,10):
    if num not in numbers:
        print("숫자 %d는 리스트에 없네요^^"%num)
        #if 항목  in 리스트 : 는 리스트에 해당 항목이 있다면 True를 반환
        #if 항목 not in 리스트 : 는 리스트에 항목이 없어야 True를 반환