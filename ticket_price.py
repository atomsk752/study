#영화관에 관객이 120명일 때 티켓 가격은 5달러이다. 영화상영비용은 180달러이며 한 사람당 추가비용 0.04달러가 든다
#티켓이 0.1달러 싸질때마다 관객이 15명 늘어난다. 티켓이 얼마일 때 최대수익을 얻는가

def make_benefit(people, ticket_price):
    income = people * ticket_price
    outcome = 180 + people * 0.04
    result = income - outcome
    return(result)

people = 120
ticket_price = 5
a = list() # 빈 리스트 생성
b = list()

for i in range(0, 50):
    money = make_benefit(people, ticket_price)
    ticket_price = round(ticket_price - 0.1, 2)
    people = people + 15
    a.append(money)
    b.append(ticket_price)

print(b[a.index(max(a))-1]) #a 리스트에서 최댓값 위치 = b 리스트 티켓값 위치
print(max(a))
