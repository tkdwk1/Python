'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 반복을 제어하는 break, continue
'''
word= input("단어를 입력하세요:") #단어 입력받기
print(":: break ::")
for i in word : #for 반복문
    if i =="a" or i=="e" or i=="o" or i=='u': #a, e, o, u가 있다면 중지
        break #반복 중단
    else:
        print(i,end='') #결과 : pr

print()
print(":: break2 ::")
for i in word : #for 반복문
    if i in ['a','e','e','o','u','A','E','I','O','U']: 
        break #반복 중단
    else:
        print(i,end='')

print()
print(":: continue ::")
for i in word : #for 반복문
    if i in ['a','e','e','o','u','A','E','I','O','U']: 
        continue #반복의 처음으로 돌아간다.
    print(i,end='') #결과 예상 prgrmmr