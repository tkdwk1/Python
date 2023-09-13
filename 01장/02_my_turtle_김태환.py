import turtle as t #터틀 모듈을 사용하기 위한 준비
                   # turtle 클래스 객채를 t로 생성
# 선 그리기
'''
t.shape('turtle')
t.speed(2)
t.forward(200)  #200px 이동


#삼각형 그리기
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
'''
'''
n =200   # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 6도 회전
    t.circle(30)
'''
for i in range(9):
    t.forward(50)
    t.left(360//9)




t.mainloop()    #그림판 사라지지 않는다