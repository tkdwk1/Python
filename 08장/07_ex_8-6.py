'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터공학부 202395012 김태환
    설명 : 심화문제 8-6
'''
student_tuple = ('211101','강이안','010-123-1111'),('211102','박동민','010-123-2222'),('211103','김수정','010-123-3333')
student_dict = {}
#딕셔너리 추가
for id, name, number in student_tuple :
    student_dict[id] = name
    
#딕셔너리 출력
for key, value in student_dict.items() :
    print(key, ":",value)

#학번 입력받아 이름과 연락처 출력
number = input("학번을 입력하시오 :")
for num in student_tuple:
    if number == num[0]:
        phone_num = num[2]
print(f"{number} 학생은 {student_dict[number]}이며, 전화번호는 {phone_num}입니다.")
