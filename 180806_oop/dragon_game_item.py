import random

class Dragon:
   def __init__(self, lev, name):
       self.lev = lev
       self.hp = lev * 10
       self.jewel = lev % 3
       self.name = name
       self.attack = self.lev * 10

   def giveJewel(self):
       return self.jewel

   def attackHero(self):
       print(self.name + ": 캬오~~~~~~~`ㅇ'")
       return random.randint(1, self.attack)

   def damage(self, amount):
       print(self.name + ": 꾸엑....................ㅠ_ㅠ")
       self.hp -= amount
       if self.hp > 0:
           print("[드래곤의 체력이", self.hp, "로 줄었다]")
       else:
           print(self.name + ": 크으으... 인간따위에게......")
       return self.hp

   def __str__(self):
       return self.name + "  레벨: " + str(self.lev)+ "  HP:" + str(self.hp)

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
           print("[플레이어의 체력이", self.hp, "로 줄었다]")
       return self.hp

   def __str__(self):
       return  self.name

class DragonContainer:

   def __init__(self, name_list):
       self.dragons = [Dragon(idx + 1, x) for idx, x in enumerate(name_list)]

   def getNext(self):
       if len(self.dragons) == 0:
           return None
       return self.dragons.pop(0)

class Colosseum:
   def __init__(self,container):
       self.container = container
       self.player = None


   def makePlayer(self):
       name = input("플레이어의 이름을 입력하시오: ")
       hp = int(input("HP는 얼마나 하겠습니까? (최대 100) "))
       self.player = Hero(name,hp)
       print("[캐릭터 "+ self.player.name,"이/가 만들어 졌습니다]")
       print("[게임을 시작합니다]")
       print("[BGM.... Start.............]")

   def fight(self):
       dragon = self.container.getNext()

       if dragon == None:
           print("[용사는 전설이 되었다]")
           return

       print("")
       print("====================================")
       print("["+dragon.name+"]"," [레벨:", str(dragon.lev)+"]","[데미지: 1 ~ "+str(dragon.attack)+"]")
       print("["+self.player.name+"]"," [HP:", str(self.player.hp)+"]",
             "[데미지: "+str(self.player.min_mp)+" ~ "+str(self.player.mp)+"]")
       print("====================================")

       while True:
           power = self.player.attackDragon()
           input("")
           print("[용사가 공격했다", "데미지:", power,"]")
           dragonhp = dragon.damage(power)
           if dragonhp <= 0:
               print("[현재 플레이어 HP: ", self.player.hp,"]")
               print("[Next Stage~]")
               jewel = dragon.giveJewel()
               if jewel == 0:
                   self.player.hp += 30
                   print("[보너스 체력이 30이 추가되었습니다]")
               random_box=random.randint(0,3)
               if random_box == 1:
                   print("[롱소드를 얻으셨습니다. 최소 공격력 증가(+10)]")
                   self.player.min_mp += 10
               elif random_box == 2:
                   print("[물약을 얻으셨습니다. HP 증가(+20)]")
                   self.player.hp += 20
               elif random_box == 3:
                   print("[갑옷을 얻으셨습니다. 드래곤 최대 데미지 감소(-10)]")
                   for x in self.container.dragons:
                       x.attack -= 10
               else:
                   print("[드래곤 사체에서 아무것도 나오지 않았습니다]")
               print("[Mission Complete]")
               break
           dragonattack=dragon.attackHero()
           print("[드래곤이",dragonattack,"만큼 데미지를 주었다]")
           herohp = self.player.damage(dragonattack)
           if herohp <= 0:
               print("["+self.player.name + "은/는 " + dragon.name +"에게 죽었습니다]")
               print("          [Game Over]")
               return

       self.fight()

name_list=["해츨링","그린드래곤","블랙드래곤","화이트드래곤","블루드래곤","실버드래곤",
          "레드드래곤","골드드래곤","레인보우드래곤","G-dragon"]
container = DragonContainer(name_list)

ground = Colosseum(container)
ground.makePlayer()
ground.fight()

