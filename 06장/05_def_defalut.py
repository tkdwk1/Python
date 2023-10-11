'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : def 예약어를 이용하여 함수 작성하고 호출하기
'''
def order1(num, pickel, onion):
    print("햄버거{}개 - 피클{}, 양파{}".format(num, pickel, onion))

#order(1) 오류발생 인자는 1개인데 매개변수는 3개이다.

#인자가 부족한 경우 기본값을 넣어주는것 => 디폴트 인자

def order2(num, pickel='기본', onion='기본'):
    print("햄버거{}개 - 피클{}, 양파{}".format(num, pickel, onion))

order2(2)
order2(1,pickel='뺌',onion'기본')