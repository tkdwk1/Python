'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 사용자가 입력하는 숫자의 합 계산하기
'''
result=int(input("숫자를 입력하시오:")) #숫자 정수로 입력받기
cont=input("계속?(yes/no):") #진행시킬건지 묻기
if cont !="no"or"yes":
    print("잘못된 입력입니다.")
while cont=="yes": #yes면 다음 숫자 받기
    num2=int(input("숫자를 입력하시오:")) #두번째 숫자 입력받기
    result=result+num2 #입력받았던 숫자 합 계산
    cont=input("계속?(yes/no):") #진행시킬건지 묻기
print("숫자의 합:",result) #입력받았던 숫자의 합 출력