import random
class Item:

    def __init__(self, str):
        self.str = str

    def __str__(self):
        return "VALUE: " + self.str


class Box:

    def __init__(self, items):
        self.items = items
        random.shuffle(self.items)

    def selectOne(self):
        return self.items.pop()


item_list = [Item('O') ] * 5
item_list.append(Item('X'))

box = Box(item_list)

for x in range(6):

    print(box.selectOne())
