#평균성적 구하기
data = [ ('진솔', 74),
         ('은상', 30),
         ('인재', 92),
         ('고은', 60),
         ('이천', 94),]
min_name = 0
min_score = 100
avg = 0

for min in data:
    if min[1] < min_score:
        min_score = min[1]
        min_name = min[0]

    avg = avg + min[1]

avg = avg / len(data)

print("평균점수: ", avg, "성적저조자: ", min_name, min_score)

