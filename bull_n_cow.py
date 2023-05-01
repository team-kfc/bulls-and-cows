import random #

correct_number = ["0", "0", "0", "0"]

correct_number[0] = str(random.randrange(1, 10, 1))
correct_number[1] = str(random.randrange(1, 10, 1))
correct_number[2] = str(random.randrange(1, 10, 1))
correct_number[3] = str(random.randrange(1, 10, 1))

while(correct_number[0] == correct_number[1]):
    correct_number[1] = str(random.randrange(1, 10, 1))
    
while(correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
    correct_number[2] = str(random.randrange(1, 10, 1)

while(correct_number[0] == correct_number[3] or correct_number[1] == correct_number[3] or correct_number[2] == correct_number[3]):
    correct_number[3] = str(random.randrange(1, 10, 1))