'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 선택문 if~else
            random을 이용한 가위바위보 게임.

            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 ==> 가위
            1 ==> 바위
            2 ==> 보

            두명의 플레이어의 이름을 입력받아 가위바위보 게임을 진행합니다.
'''
import random #random 함수 가져오기

print(":: 가위 바위 보 게임 시작 ::")

player1=input('플레이어1 의 이름:')
player2=input('플레이어2 의 이름:')

num1=random.randrange(3) #랜덤으로 0, 1, 2생성
num2=random.randrange(3) #랜덤으로 0, 1, 2생성
print()
print(player1,':',end='')
if num1==0:
    print("가위")
elif num1==1:
    print("바위")
elif num1==2:
    print("보")

print(player2,':',end='')
if num2==0:
    print("가위")
elif num2==1:
    print("바위")
elif num2==2:
    print("보")
print()
if (num1==0 and num2==1) or (num1==1 and num2==2) or (num1==2 and num2==0):
    print('플레이어',player2,'이(가) 이겼습니다')
elif (num2==0 and num1==1) or (num2==1 and num1==2) or (num2==2 and num1==0):
    print('플레이어',player1,'이(가) 이겼습니다.')
else:
    print('비겼습니다.')