'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 조건에 따라 반복하는 while문
'''
#while 조건식 : --> : 반드시 사용.
#   들여쓰기로 반복하며 할일 작성

#반복문에는 반드시 종료문구가 있어야한다.
#while True: 무한반복
under_construction=True #공사중

# True일 동안 계속 반복
while under_construction :
    response = input("공사가 완료되었습니까?")
    if response == "예":
        under_construction = False #공사 완료

print("루프탈출")