'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 돌려주는 함수.

    리스트에 10개의 값을 랜덤으로 생성하고,
    max또는 min을 입력받아 최대, 최솟값을 찾아 돌려주는 함수.

    (함수)
        5)두 값을 전달받아 매개변수에 저장.
        6)최대값, 최소값을 찾는다.
        7)값을 돌려준다
    (메인)
        1.무한반복
            1)랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2)생성된 리스트를 출력
            3)사용자로부터 최대값을 알고싶은지, 최솟값을 알고싶은지 묻는다.
                사용자가 입력할 값는 max또는 min
            4)입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8)돌려받은 최대값 또는 최솟값을 출력한다
'''
def getMinMax(list_data,method='max'):
    min=100
    max=1
    
    if method == 'max':
        for i in list_data:
            if i > max:
                max = i
        return max
    if method == 'min':
        for i in list_data:
            if i < min:
                min = i
        return min
    
import random #random 함수 가져오기

while True:
    list=random.sample(range(10,99),10) #랜덤으로 10개의 수 생성
    print(list)
    s=input("최대값을 원하면 max, 최소값을 원하면 min을 입력해주세요. :") #사용자로부터 최대값을 알고싶은지, 최솟값을 알고싶은지 입력받기
    print(getMinMax(list,s)) #돌려받은 최대값 또는 최솟값을 출력

    