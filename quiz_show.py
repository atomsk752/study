quiz_list = [
    {"title":"다음 중 좀비가 나오는 게임은? ","desc":"1. 리그오브레전드  2. 철권 3. 스타크래프트 4. 마인크래프트 ", "answer": 4},
    {"title": "다음 중 가장 출시된지 오래된 게임은? ", "desc": "1. 스타크래프트 2. 소닉 3. 바람의나라 4. 리니지 ", "answer": 2},
    {"title": "다음 중 MMORPG가 아닌 게임은? ", "desc": "1. 아이언사이트   2. 믹스마스터  3. 테일즈위버  4. 아키에이지 ", "answer": 1},
    {"title": "2018년 8월 기준으로 동시접속자가 가장 많은 게임은?", "desc": "1. 리그오브레전드 2. 오버워치 3. 메이플스토리 4. 배틀그라운드 ", "answer": 4},
    {"title": "고전 포켓몬스터 게임에서 치트를 쓰지 않고 세레비를 잡을 수 있는 버전은?", "desc": "1. 골드 2. 파이어레드 3. 크리스탈 4. 소울실버 ", "answer": 3},
    {"title":"다음의 모바일 게임중 카카오에서 서비스 하지 않는 게임은? ","desc":"1. 드래곤네스트 2. 소녀전선 3. 프렌즈팝  4. 데스티니 차일드 ", "answer": 2},
    {"title":"다음의 모바일 게임중 PC버전이 없는 게임은?","desc":"1. 이카루스  2. 그랜드체이스  3. 이터널 라이트  4. 천년지애  ", "answer": 3},
]
print("게임을 시작합니다.")

a=0
for quiz in quiz_list:
    print(quiz['title'])
    print(quiz['desc'])
    ans=int(input("정답은 무엇입니까? "))

    if ans == quiz['answer']:
        a += 1
        print("정답입니다.")
    else:
        print(str(a)+"개 맞추셨습니다.")
        print("Game over")
        break

    if a == 7:
         print("당신은 퀴즈왕입니다!!!")
         break
