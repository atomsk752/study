import math

class Store:

   def __init__(self, name, menu, lat, lng):
       self.name = name
       self.menu = menu
       self.lat = lat
       self.lng = lng

   def calc_distance(self, target_lat, target_lng):

       distance = math.sqrt(math.pow(target_lat - self.lat, 2) + math.pow(target_lng - self.lng , 2))

       return distance

   def __str__(self):
       return self.name

class StoreFinder:

   def __init__(self):
       self.stores = [
           Store('쭉심', '쭈꾸미삼겹살', 37.531675, 126.86300),
           Store('계열사', '치킨', 37.592935, 126.966215),
           Store('형제육회', '육회비빔밥', 37.570613, 126.999985),
           Store('청진옥', '수육', 37.571708, 126.979419),
           Store('종로진낙지', '낙지', 37.572151, 126.989094),
           Store('엄지네포장마차', '꼬막비빔밥', 37.766558, 128.907029)]

   def find(self, lat, lng):
       self.stores.sort(key = lambda store: store.calc_distance(lat,lng ) * 10000000)

       return self.stores[0]

class UI:
   def __init__(self):
       self.finder = StoreFinder()

   def ui(self):
       lat = float(input("경도를 입력하세요: "))
       lng = float(input("위도를 입력하세요: "))
       result = self.finder.find(lat,lng)
       print(result.name, result.menu)


result = UI()
result.ui()


