from random import randint
print("welcome to guessing the number game!\n")
print('''
                                                __  .__                                         ___.                 
   ____  __ __   ____   ______ ______         _/  |_|  |__   ____             ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/  ______ \   __\  |  \_/ __ \   ______  /    \|  |  \/     \| __ \_/ __ \_  __ \\
 / /_/  >  |  /\  ___/ \___ \ \___ \  /_____/  |  | |   Y  \  ___/  /_____/ |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >          |__| |___|  /\___  >         |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/                     \/     \/               \/            \/    \/     \/       
                                                                                                                     
''')
difficulty = input("choose the difficulty, type 'easy' or 'hard'\n")
level = {
    'easy': [10, "you will have 5 attempts in guessing the number\n"],
    'hard': [5, "you will have 5 attempts in guessing the number\n"]
}
print(level[difficulty][1])
guess = int(input("guess a number within 1 to 100\n"))
i = 1
actual_num = randint(1, 100)
# print(f"actual number was {actual_num}\n")
while i <= level[difficulty][0]:
    if actual_num == guess:
        print("congrats! you guessed the correct number\n")
        i = level[difficulty][0] + 1
    elif actual_num > guess:
        print(f"the guessed number is low\nchances left are {level[difficulty][0] - i}\nguess again\n")
    else:
        print(f"the guessed number is high\nchances left are {level[difficulty][0] - i}\nguess again\n")
    i = i + 1
    if i <= level[difficulty][0]:
        guess = int(input("guess a number \n"))
print(f"actual number was {actual_num}\n")
