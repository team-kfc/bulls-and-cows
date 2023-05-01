print("숫자야구 게임에 오신 여러분 환영합니다.")

import random #파이썬 랜덤 모듈
correct_number = ["0", "0", "0", "0"] #파이썬에서 input() 함수의 사용자 입력은 문자열이므로 "0" 문자열로 배열
correct_number[0] = str(random.randrange(1, 10, 1))
correct_number[1] = correct_number[0]
correct_number[2] = correct_number[0]
correct_number[3] = correct_number[0]

# 랜덤 숫자가 같다면 계속 반복
while(correct_number[0] == correct_number[1]):
    correct_number[1] = str(random.randrange(1, 10, 1))
while(correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
    correct_number[2] = str(random.randrange(1, 10, 1))
while(correct_number[0] == correct_number[3] or correct_number[1] == correct_number[3] or correct_number[2] == correct_number[3]):
    correct_number[3] = str(random.randrange(1, 10, 1))

print(correct_number)

try_number = 0
strike_number = 0
ball_number = 0

print("숫자야구를 시작합니다.")
print("--------------------------")
while (strike_number < 4):

    number = str(input("숫자 4자리를 입력하세요: "))

    strike_number = 0
    ball_number = 0

    for i in range(0, 4): # i 값의 범위 0~3
        for j in range(0, 4):
            if(number[i] == str(correct_number[j]) and i == j):
                strike_number += 1
            elif(number[i] == str(correct_number[j]) and i != j):
                ball_number += 1
    print("결과: [",strike_number,"]스트라이크 [",ball_number,"]볼")
    try_number += 1

print("--------------------------")
print("축하합니다! 정답입니다!")
print("[",try_number,"]번 만에 맞췄습니다")