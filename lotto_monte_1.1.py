#Step 1 - 1000개의 리스트
#내용물은 1에서 45까지의 숫자 - arr
from random import randint

arr = [randint(1,45) for x in range(1000)]


#Step 2 - 어떤 숫자가 많이 나왔는지

record = [0] * 45


for num in arr:
    record[num-1] += 1

print(record)

for idx, count in enumerate(record):
    print(idx + 1, "  COUNT: ", count)
#Step 3 - 숫자들 중에서 가장 많이 나온 숫자 알아내기

max = 0
max_id = 0

for idx, count in enumerate(record):
    if count > max:
        max = count
        max_id = idx


print("MAX NUM: ", (max_id)+1)
print("MAX", max)

# 리스트를 만들어서 정렬하기

def maxnum2(max2, max_id2):
    arr2 = [randint(1,45) for x in range(1000)]

    record2 = [0] * 45

    for num2 in arr2:
        record2[num2-1] += 1

    for idx2, count2 in enumerate(record2):
        if count2 > max2:
            max2 = count2
            max_id2 = idx2
    return max2

max2 = 0
max_id2 = 0

maxnum2(max2, max_id2)



print("MAX2 NUM: ", (max_id2)+1)
print("MAX2", max2)