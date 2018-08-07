import random

class Dragon:
   def __init__(self, lev, name):
       self.lev = lev
       self.hp = lev * 10
       self.name = name
       self.jewel = random.randint(1, 4)

   def giveJewel(self):
       return self.jewel

   def attackHero(self):
       print(self.name, ": 캬오~~~~~~~`ㅇ'")
       return random.randint(1, (self.lev * 10))

   def damage(self, amount):
       print(self.name, ": 꾸엑....................ㅠ_ㅠ")
       self.hp -= amount
       if self.hp > 0:
           print("<SYSTEM>: 용의 체력이", self.hp, "로 줄었다.")
       else:
           print(self.name, ": 분하다....하지만 나는 사천왕중 최약체...")
       return self.hp

   def __str__(self):
       return "용 레벨" + str(self.lev)+ ":" + str(self.hp) + ":" + str(self.name)

class Hero:

   def __init__(self, name, hp):
       self.name = name
       self.hp = hp
       self.mp = 100 - hp
       self.min_mp = 1

   def attackDragon(self):
       return random.randint(self.min_mp, self.mp)

   def damage(self, amount):
       print(self.name+": 윽....................ㅠ_ㅠ")
       self.hp -= amount
       if self.hp > 0:
           print("<SYSTEM>: 플레이어의 체력이", self.hp, "로 줄었다.")
       else:
           print("<SYSTEM>: 용사는 드래곤의 훌륭한 단백질 공급원이죠.")
           print("<SYSTEM>: Game over")
       return self.hp

   def __str__(self):
       return  self.name + "님" +" HP- " + str(self.hp) + ", MP-" + str(self.mp)

class DragonContainer:

   def __init__(self, name_list):
        self.dragons = [ Dragon(idx + 1, x) for idx, x in enumerate(name_list)]

   def getNext(self):
       if len(self.dragons) == 0:
           return None
       return self.dragons.pop(0)


class Colosseum:
   def __init__(self, container):
       self.container = container
       self.player = None


   def makePlayer(self):
       name = input("당신의 이름을 알려주시오, 용사여\n 나는... : ")
       hp = int(input("HP는 얼마나 하겠습니까? (최대 100) "))
       self.player = Hero(name,hp)
       print("<SYSTEM>:", name,"님 부디 용을 물리쳐주세요!")

   def fight(self):
       input("")
       print("<SYSTEM>: 간다앗!!!!!")
       print("<SYSTEM>: BGM.... Start........둥칫둥칫")
       dragon = self.container.getNext()

       if dragon == None:
           print("<SYSTEM>: 용사는 전설이 되었다.")
           return

       print(dragon)

       while True:
           power = self.player.attackDragon()
           input("")
           print("<SYSTEM>: 용사가 공격했다", "데미지:", power)
           dragonhp = dragon.damage(power)
           if dragonhp <= 0:
               jewel = dragon.giveJewel()
               print("<SYSTEM>: 용이 사망하였습니다.")
               if jewel == 1:
                   heal = random.randint(20, 50)
                   self.player.hp += heal
                   print("<SYSTEM>: 용이 심장을 떨어뜨렸습니다.", heal, "만큼 체력이 회복됩니다.")
               elif jewel == 2:
                   upgrade = random.randint(5, 20)
                   self.player.min_mp += upgrade
                   self.player.mp += upgrade
                   print("<SYSTEM>: 드래곤의 발톱으로 검을 강화했습니다. (공격력",upgrade, "증가)")
               elif jewel == 3 or 4:
                   print("<SYSTEM>: 아무일도 일어나지 않았습니다.")
               break
           dragonattack=dragon.attackHero()
           print("<SYSTEM>: 용이 ", dragonattack,"만큼 데미지를 주었다.")
           herohp = self.player.damage(dragonattack)
           if herohp <= 20:
               upgrade1 = random.randint(30, 60)
               self.player.min_mp += upgrade1
               self.player.mp += upgrade1
               print("<SYSTEM>: 위험에 처한 용사가 각성했습니다. (공격력", upgrade1, "증가)")
               if herohp <= 0:
                   return

       self.fight()

dragonNames = ['뀽뀽이', '투명드래곤', '꺵깽이', '이무기', '용가리',
                           '닥터드래곤', '이소룡', '개밥바리기', '용신', '고질라', '데스윙',]

container = DragonContainer(dragonNames)

# for x in range(10):
#    print(container.getNext())
#용이 다 죽으면 None:

ground = Colosseum(container)
ground.makePlayer()
ground.fight()
