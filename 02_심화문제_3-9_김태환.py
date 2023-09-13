'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 90페이지 문제 3-9
        평균 시속과 이동시간을 입력받아
        이동시간은 시,분,초 단위로 출력하고,
        이동한 거리를 계산하여 출력하시오
'''
perhour=float(input("평균 시속(km/h)를 입력하세요 :"))
time=float(input("이동 시간(h)을 입력하세요 :"))
total_time = time * 3600  # 토탈 걸린 시간
hour = total_time // 3600  # 시 부분을 계산
minite = (total_time % 3600) // 60  # 분 부분을 계산
sec = total_time % 60  # 초 부분을 계산

print(
    "평균 시속 : {} km/h \n이동 시간 : {:.0f} 시간 {:.0f} 분 {:.0f} 초 \n이동 거리 : {} km".format(perhour, hour, minite, sec, perhour * time)
)