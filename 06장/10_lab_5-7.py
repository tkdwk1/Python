'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 단을 입력 받아 해당 단의 구구단을 출력하시오

    문제 분석:단은 고정
        곱하는 수 시작값:1
        곱하는 수 종료값:9
        곱하는 수 증가값:1

    필요한 변수:num, sum , multi
'''
num=int(input("단 입력:"))
sum=0
while sum <= 8:
    sum=sum+1
    multi=sum*num
    print(multi)