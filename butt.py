import random

some_input = input("What did are you trying to translate: ") 
str_arry = some_input.split()
butt_arry = ["OBEY","CONSUME","THIS IS YOUR GOD","CONFORM","SUBMIT"]
output = ""
random_num = 0
for s in str_arry:
    random_num = random.randrange(4)
    output = output + butt_arry[random_num] + " "
print(output)