try_number = 0
strike_number = 0
ball_number = 0

print("숫자여구를 시작합니다.")
print("---------------------")

while(strike_number < 4):
    number =  str(input("숫자 4자리를 입력하세요: "))
    
    strike_number = 0
    ball_number = 0
    
    for i in range(0, 4):
        for j in range(0, 4):
            if(number[i] == str(correct_number[j]) and i == j):
                strike_number += 1
            elif(number[i] == str(correct_number[j]) and i != j):
                 ball_number += 1
    print("결과: [",strike_number,"]bulls [",ball_number,"]cows")
    try_number += 1
