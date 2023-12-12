#사용자한테 비번 갯수를 입력받아 랜덤비번 생성하기 이때 str()함수로 변환하여 랜덤수를 더하여 최종적으로 비번 만들기 -
import random as rd
num_length = int(input("몇 자리의 비밀번호를 원하십니까? : "))

otp = ""
for i in range(num_length):
  otp += str(rd.randrange(0, num_length))
print(otp)