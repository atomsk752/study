import random
class LottoBall:
    def __init__(self,num):
        self.num = num
        self.selected = False

    def isSelected(self):
        answer = self.selected
        self.selected = True
        return answer

    def __str__(self):
        return  str(self.num)


balls = [LottoBall(x) for x in range(46)]
print(balls)

count = 0

while count < 6:

    idx = random.randint(1,44)

    aball = balls[idx]

    if aball.isSelected() == True:
        print("중복발생", aball)
        continue

    print(aball)

    count += 1