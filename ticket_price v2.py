#영화관에 관객이 120명일 때 티켓 가격은 5달러이다. 영화상영비용은 180달러이며 한 사람당 추가비용 0.04달러가 든다
#티켓이 0.1달러 싸질때마다 관객이 15명 늘어난다. 티켓이 얼마일 때 최대수익을 얻는가

def make_benefit(people, ticket_price):
    income = people * ticket_price
    outcome = 180 + people * 0.04
    result = income - outcome
    return(result)

people = 120
ticket_price = 5
max = 0

for i in range(0, 50):
    money = make_benefit(people, ticket_price)

    if money > max:
        max = money
        max_ticket_price = ticket_price

    else:
        break

    ticket_price = ticket_price - 0.1
    people = people + 15

print('%.2f' % max_ticket_price, ":",'%.2f' % max)