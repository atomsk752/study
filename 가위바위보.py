# com - user = 2 컴이 이김
# com - user = 1 유저가 이김
# com - user = 0 비김
# com - user = -1일때 +3 컴 이김
# rock 0 sissor 1 paper 2 중 하나를 넣으면 승무패 결과값 출력
# com 보 user 바위


import random
win = 0
lose = 0
draw = 0

for i in range(0, 10):
    user = input("rock or scissor or paper or stop \n")

    if user == 'stop':
        break
    if user == 'rock':
        user = 0
    elif user == 'scissor':
        user = 1
    elif user == 'paper':
        user = 2

    print("-----------------------")

    com = random.randint(0, 2)
    print(com)
    if com < user:
        com = com + 3
    result = com - user

    print("-----------------------")

    if result == 1:
        win = win + 1
        print("WIN", win)
    elif result == 2:
        lose = lose + 1
        print("LOSE", lose)
    elif result == 0:
        draw = draw + 1
        print("DRAW", draw)

print("WIN", win, "LOSE", lose, "DRAW", draw)