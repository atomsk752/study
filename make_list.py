
#arr = input('Atteibute name') #이런 식으로 호출가능
#data["price"] = 5500 #내부값변경
#while 루프를 사용한 의사결정트리
#print(data[arr])
s1 = {"name":"KFC",
      "addr":"zonggak-4",
      "price":5000,
      "next": None}

s2 = {"name":"Buger King",
      "addr":"종각4거리 KFC옆",
      "price":6000,
      "next": None}
s3 = {"name":"mom's touch",
      "addr":"종각 지하철 옆",
      "price":5500,
      "next": None}
s1['next'] = s2
s2['next'] = s3

#while 루프는 몇번해야 할지 모를때

current = s1

while True:
    if current == None:
        print("그만먹어")
        break
        
    print(current['name'], '에 도착하였습니다')
    oper = input("또 먹어? y/n")
    if oper == 'y':
        current = current['next']
    else:
        print('오늘은 여기까지')
        break
