from random import randint
arr=[randint(1, 45) for x in range(1000)]

result = [{"name": x, "count" : 0} for x in range(1, 46)]

for num in arr:
    result[num - 1]["count"] += 1

lotto=[]

for k in range(6):
    max = 0
    max_index = 0

    for idx, x in enumerate(result):

        if x['count'] > max:
            max = x['count']
            max_index = idx

    lotto.append(result.pop(max_index)['name'])

print(lotto)