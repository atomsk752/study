import math

data=[{"genre": "Action", "x": 12, "y": 2, "title": "DarkKnight"},
     {"genre": "Action", "x": 6, "y": 4, "title": "Inception"},
     {"genre": "Melo", "x": 2, "y": 4, "title": "BeforeSunRise"},
     {"genre": "Melo", "x": 1, "y": 8, "title": "HereToCome"},
     {"genre": "Melo", "x": 3, "y": 6, "title": "NottingHill"},
     {"genre": "Action", "x": 9, "y": 1, "title": "KillBill"}]


movie_title = input("Movie Name: ")

target = None

for movie in data:
    if movie['title'] == movie_title:
        target = movie


print("=============================")
print(target)


def calc_distance(p1):
    distance = math.pow(target['x'] - p1['x'], 2) + math.pow(target['y'] - p1['y'], 2)
    return distance


data.sort (key = calc_distance)
data.pop(0)

print(data["title"])

# for point in data:
#     print(point)
#     result = calc_distance(target, point)
#     print(result)


# (x - y)**2+(x'-y')**2d