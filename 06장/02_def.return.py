'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 반지름 값을 받아 넓이를 구하고 넓이를 올려주는 함수를 작성
        함수-생성이 우선 area
        2. 반지름 값을 전달받아 매개변수에 저장
        3. 반지름으로 원의 넓이를 계산한다
        4. 계산된 넓이를 함수를 호출한 곳으로 돌려준다

        <함수 호출하는 메인>
        1. 반지름은 가지고 함수를 호출한다
        5. 돌려받은 넓이를 출력한다
'''

print("::리터값이 있는 함수 (원의 넓이 구하기)::")

#함수 선언
def area(radius):
    result=3.14*radius**2
    return result
result=area(3)
print(f"반지름이 3인 원의 넓이는 {result}입니다.")

print()
print("::반지름을 입력받아 원의 넓이 계산하기::")
r=int(input("반지름을 입력하시오 :"))
result=area(r) #전달받은 결과를 result에 저장
print(f"반지름이 {r}인 원의 넓이는 {result}입니다.") #result에 저장된 결과를 출력

print()

#반지름을 가지고 함수 호출, 전달받아 바로 출력
print(f"반지름이 {r}인 원의 넓이는 {area(r)}입니다.")