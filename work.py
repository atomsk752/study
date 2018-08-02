#주일하는 일자 다름
#얼마 줘야하는지
#일 8시간
#최저시급7530원
#월 일한 날짜 월급
#월급 = 일한시간 * 최저임금
#일한시간 = 출근일(월) * 8
#최저임금계산 = 7530
#날짜 or 시간

oper = input("D or H \n")
if oper == 'D':
    print("날짜로 계산합니다.")
    day = int(input("몇 일 근무했습니까 \n"))
    salary = day * 8 * 7530
    print(salary)
elif oper == 'd':
     print("날짜로 계산합니다.")
     day = int(input("몇 일 근무했습니까 \n"))
     salary = day * 8 * 7530
     print(salary)
elif oper == 'H':
    print("시간으로 계산합니다.")
    hour = int(input("몇 시간 근무하였습니까 \n"))
    salary = hour * 7530
    print(salary)
elif oper == 'h':
    print("시간으로 계산합니다.")
    hour = int(input("몇 시간 근무하였습니까 \n"))
    salary = hour * 7530
    print(salary)
