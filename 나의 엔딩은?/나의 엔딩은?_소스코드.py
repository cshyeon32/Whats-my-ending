import random
import time
import sys  # 색 함수
import json

# 색상 정의
class c:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class b:
    RED = '\033[41m'
    BLUE = '\033[44m'
    WHITE = '\033[47'

# 함수 정의
def option3():
    print("3개 중 당신이 원하는 선택지의 번호를 1개 입력하세요.")


def option4():
    print("4개 중 당신이 원하는 선택지의 번호를 1개 입력하세요.")


def back():
    num = int(input(c.RED + "숫자를 잘못 입력하셨습니다. 다시 입력해 주세요") + c.RESET)
    time.sleep(2)


# 호감도 데이터를 저장하고 불러올 파일 경로
data_file = "likability_data.json"


# 호감도 데이터를 저장하는 함수
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)


# 호감도 데이터를 불러오는 함수
def load_data():
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
            # 호감도가 큰 순서대로 정렬
            sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
            return sorted_data
    except FileNotFoundError:
        return {}


def check_word(sentence, target_word):
    words = sentence.split()
    for word in words:
        if word.lower() == target_word.lower():  # 대소문자 구분 없이 단어를 비교합니다.
            return True
    return False
target_word = ("미안")

# 호감도가 0 이하가 되면 게임 종료
def neg(likability):
    if likability < 0:
        print(b.WHITE + c.BLUE + "*****당신은 실패했습니다.*****" + c.RESET)
        print(c.CYAN + "호감도가 마이너스가 되었습니다.")
        print("당신은 더 이상 책 속에서 탈출하지 못합니다.")
        print("다시 도전하세요" + c.RESET)
        sys.exit()


# 프로그램 시작
def start_program():
    # 호감도 데이터 불러오기
    likability_data = load_data()
    likability = 10
    #시작
    print("안녕하세요!"+c.RESET)
    time.sleep(2)
    print("당신은 지금 책 속으로 들어오셨습니다."+c.RESET)
    time.sleep(2)
    print("주인공의"+c.GREEN+" 호감도를 100으로 만들어 이 책 속에서 탈출하세요!"+c.RESET)
    time.sleep(2)
    print(c.GREEN+"(시작 호감도는 10입니다. 만약 호감도가 0 미만이 되면 당신은 실패입니다.)"+c.RESET)
    time.sleep(2)
    name=input(c.UNDERLINE +"당신의 이름을 입력하세요:")
    gender=int(input(name+"님 "+c.MAGENTA+"0=여자, 1=남자"+c.RESET+c.UNDERLINE +" 성별을 숫자로 입력해주세요:"+c.RESET))
    time.sleep(2)
    while 1:
        if gender==0:
            x=input(c.UNDERLINE +"당신의 남자주인공 이름을 입력하세요:"+c.RESET)
            break
        elif gender==1:
            x=input(c.UNDERLINE +"당신의 여자주인공 이름을 입력하세요:"+c.RESET)
            break
        else:
            gender=int(input(c.RED+"성별을 잘못 입력하셨습니다. 다시 입력해 주세요"+c.RESET))
    time.sleep(2)

        #첫날 시작
    print()
    print(b.BLUE+"첫 번째 날"+c.RESET)
    print()
    time.sleep(2)
    print("당신은 지금 당신이 즐겨보던 책 속에서 눈을 떴습니다."+c.RESET)
    time.sleep(2)
    print(x+"는(은)"+c.YELLOW+" 평소 고기와 해산물류를 좋아하고 배드민턴 치는 것을 좋아하고 요가를 싫어합니다."+c.RESET)
    time.sleep(2)
    print(x+"(이)가 지금 같이 점심을 먹자고 합니다. "+c.UNDERLINE +"메뉴는?"+c.RESET)
    time.sleep(2)
    option3()
    time.sleep(2)
    print(c.MAGENTA+"1:채소류, 2:고기류, 3:해산물류"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(1,10)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        elif num==2:
            ran=random.randint(5,10)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==3:
            ran=random.randint(1,5)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()
    

    print("당신은 "+x+"와 아침을 먹으면서 이야기하다 "+x+"(이)가 싫어하는 것들을 알게 되었다."+c.RESET)
    time.sleep(2)
    print(x+"(이)가 "+c.YELLOW+"싫어하는 음식은 쓴 음식과 민트초코, 하와이안 피자라고 한다."+c.RESET)
    time.sleep(2)
    print("당신은 밥을 다 먹고 "+x+"와 함께 산책하러 가기로 했다."+c.RESET)
    time.sleep(2)
    print("산책하다 근처 카페에 들어왔다."+c.RESET)
    time.sleep(2)
    print(x+"(이)가 알아서 자신의 것까지 메뉴를 고르라 한다."+c.RESET)
    time.sleep(2)
    print(x+"(이)가 "+c.UNDERLINE +"먹을 메뉴는?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:딸기 라떼, 2:아이스 아메리카노, 3:민트초코 아이스크림, 4:쿠키"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(5,10)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(1,5)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        elif num==3:
            ran=random.randint(5,10)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        elif num==4:
            ran=random.randint(1,5)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()


    print("카페에서 이야기하다가 "+x+"(이)가 내가 좋아하는 운동이 있으면 같이하자고 합니다."+c.RESET)
    time.sleep(2)
    sport=str(input(c.UNDERLINE +"좋아하는 운동"+c.RESET+"을 입력하세요:"))
    if sport=="배드민턴":
        ran=random.randint(10,15)
        print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
        likability+=ran
    elif sport=="요가":
        ran=random.randint(5,10)*-1
        print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
        likability+=ran
        neg(likability)
    else:
        ran=random.randint(1,15)
        print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
        likability+=ran
    time.sleep(2)

    print("당신은 지금 "+x+"와 "+sport+"하고 "+c.UNDERLINE +"저녁을 먹기 위해 식당을 고르는 중입니다."+c.RESET)
    time.sleep(2)
    option3()
    time.sleep(2)
    print(c.MAGENTA+"1:조용하고 비싼 식당, 2:시끌벅적한 포장마차, 3:적당히 시끄러운 가성비 좋은 뷔페"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(5,10)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(1,10)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        elif num==3:
            ran=random.randint(5,10)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()

    

    print("밥을 먹다 보니 당신은 "+c.UNDERLINE +"목이 말라 마실 것을 시키려고 합니다."+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:제로 콜라, 2:맥주, 3:사이다, 4:소주"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(1,5)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        elif num==3:
            ran=random.randint(5,10)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==4:
            ran=random.randint(5,10)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        else:
            back()

    print("당신은 지금 "+x+"(이)와 밥을 다 먹고 헤어지고 난 후 집에 돌아와 침대에 누웠습니다."+c.RESET)
    time.sleep(2)
    print("내일은 "+x+"(이)의 생일입니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 선물을 주어야 할까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:지금 가장 잘나가는 향수, 2:지갑, 3:손목시계, 4:빔프로젝터"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(5,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(5,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==3:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==4:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()

    # 지금까지 호감도 출력
    print(c.RED+"지금까지 "+x+"(이)의 호감도는 %d 입니다."%likability+c.RESET )
    print()
    #두번째날
    time.sleep(5)
    print(b.BLUE+"두 번째 날"+c.RESET)
    print()
    time.sleep(3)
    print("오늘 점심을 먹고 같이 영화를 보기로 하였습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 옷을 입고 가야 할까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    if gender==0:
        print(c.MAGENTA+"1:무난한 원피스, 2:시즈니 룩, 3:화려한 드레스, 4:호피 무늬 옷"+c.RESET)
        num=int(input())
        while 1:
            if num==1:
                ran=random.randint(10,15)
                print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
                likability+=ran
                break
            elif num==2:
                ran=random.randint(1,5)*-1
                print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
                likability+=ran
                neg(likability)
                break
            elif num==3:
                ran=random.randint(5,10)*-1
                print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
                likability+=ran
                neg(likability)
                break
            elif num==4:
                ran=random.randint(5,10)*-1
                print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
                likability+=ran
                neg(likability)
                break
            else:
                back()
    else:
        print(c.MAGENTA+"1:남친 룩, 2:모나미 룩, 3:체육복, 4:스키니진"+c.RESET)
        num=int(input())
        while 1:
            if num==1:
                ran=random.randint(10,15)
                print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
                likability+=ran
                break
            elif num==2:
                ran=random.randint(1,5)*-1
                print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
                likability+=ran
                neg(likability)
                break
            elif num==3:
                ran=random.randint(5,10)*-1
                print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
                likability+=ran
                neg(likability)
                break
            elif num==4:
                ran=random.randint(5,10)*-1
                print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
                likability+=ran
                neg(likability)
                break
            else:
                back()

    print("약속한 시간이 되고"+c.RESET)
    time.sleep(2)
    print("당신은 지금",x+"(이)를 만났습니다."+c.RESET)
    time.sleep(2)
    print(x+"(이)는 지금 배가 많이 고픈 상태입니다."+c.RESET)
    time.sleep(2)
    print("당신들 앞에는 지금 3개의 식당이 있습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 식당을 가야할까요?"+c.RESET)
    time.sleep(2)
    option3()
    time.sleep(2)
    print(c.MAGENTA+"1:분식집, 2:족발집, 3:마라탕집"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(5,10)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==3:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",random.randint(10,15),"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()

    if num==1:
        print("당신은",x+"(이)와 함께 분식집에서 밥을 다 먹었습니다."+c.RESET)
    elif num==2:
        print("당신은",x+"(이)와 함께 족발집에서 밥을 다 먹었습니다."+c.RESET)
    elif num==3:
        print("당신은",x+"(이)와 함께 마라탕집에서 밥을 다 먹었습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 영화를 볼까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:공포 영화, 2:로맨스 영화, 3:스포츠 영화, 4:액션 영화"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==3:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==4:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()
    print(x+"(이)가 영화가 너무 재미있었다고 합니다."+c.RESET)
    time.sleep(2)
    ran=random.randint(1,5)
    print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
    likability+=ran
    time.sleep(2)
    print("당신과",x+"(이)는",x+"(이)가 좋아하는 디저트 집에 왔습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 디저트를 먹어야 할까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:약과 쿠키, 2:푸딩, 3:빙수, 4:빵"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==3:
            ran=random.randint(10,20)*-1
            print(x+"는 카페가 추워서 빙수를 먹고 싶어 하지 않았습니다.")
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        elif num==4:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        else:
            back()

    print("밥을 먹으러 식당에 왔습니다."+c.RESET)
    time.sleep(2)
    print(x+"(이)는 "+c.YELLOW+"고르곤졸라 피자를 시켰습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"당신이 먹을 음식을 고르세요."+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:김치베이컨 필라프, 2:매콤 봉골레, 3:새우 누룽지 알리오올리오, 4:고르곤졸라 피자"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==2:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==3:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            break
        elif num==4:
            ran=random.randint(10,20)*-1
            print(c.CYAN+"호감도가",ran,"% 감소했습니다."+c.RESET)
            likability+=ran
            neg(likability)
            break
        else:
            back()

    print("밥을 다 먹고 산책하면서 "+x+"에게 내일 뭘 할지 물어봤습니다."+c.RESET)
    time.sleep(2)
    print(x+"(이)가 놀이공원에 가자고 합니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 놀이공원에 갈까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:이월드, 2:서울 롯데월드, 3:에버랜드, 4:부산 롯데월드"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            apark="이월드"
            time.sleep(2)
            print("내일 아침 10시에 "+x+"(이)와 이월드에서 만나기로 했습니다."+c.RESET)
            break
        elif num==2:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            apark="서울 롯데월드"
            time.sleep(2)
            print("내일 아침 10시에 "+x+"(이)와 서울 롯데월드에서 만나기로 했습니다."+c.RESET)
            break
        elif num==3:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            apark="에버랜드"
            time.sleep(2)
            print("내일 아침 10시에 "+x+"(이)와 에버랜드에서 만나기로 했습니다."+c.RESET)
            break
        elif num==4:
            ran=random.randint(10,15)
            print(c.CYAN+"호감도가",ran,"% 올랐습니다."+c.RESET)
            likability+=ran
            apark="부산 롯데월드"
            time.sleep(2)
            print("내일 아침 10시에 "+x+"(이)와 부산 롯데월드에서 만나기로 했습니다."+c.RESET)
            break
        else:
            back()
    time.sleep(2)
    print("산책을 끝마치고 각자 집에 가기로 합니다."+c.RESET)
    time.sleep(2)
    print(c.YELLOW+"집까지는 걸어서 25분이 걸립니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 방법으로 갈까?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:택시, 2:지하철, 3:버스, 4:자전거"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            print(c.CYAN+"호감도가",random.randint(10,20)*-1,"% 감소했습니다."+c.RESET)
            neg(likability)
            time.sleep(2)
            print(x+"(이)는 당신과 같이 있기 위해서 당신의 집까지 걸어서 데려다주고 싶어 했습니다."+c.RESET)
            break
        elif num==2:
            print(c.CYAN+"호감도가",random.randint(10,20)*-1,"% 감소했습니다."+c.RESET)
            neg(likability)
            time.sleep(2)
            print(x+"(이)는 당신과 같이 있기 위해서 당신의 집까지 걸어서 데려다주고 싶어 했습니다."+c.RESET)
            break
        elif num==3:
            print(c.CYAN+"호감도가",random.randint(10,20)*-1,"% 감소했습니다."+c.RESET)
            neg(likability)
            time.sleep(2)
            print(x+"(이)는 당신과 같이 있기 위해서 당신의 집까지 걸어서 데려다주고 싶어 했습니다."+c.RESET)
            break
        elif num==4:
            print(c.CYAN+"호감도가",random.randint(10,20)*-1,"% 감소했습니다."+c.RESET)
            neg(likability)
            time.sleep(2)
            print(x+"(이)는 당신과 같이 있기 위해서 당신의 집까지 걸어서 데려다주고 싶어 했습니다."+c.RESET)
            break
        else:
            back()

    # 지금까지 호감도 출력
    print(c.RED+"지금까지 "+x+"(이)의 호감도는 %d 입니다."%likability+c.RESET )

    #마지막날
    time.sleep(5)
    print()
    print(b.BLUE+"세 번째 날"+c.RESET)
    print()
    time.sleep(3)
    print("당신은 어제 일찍 잠이 들었습니다."+c.RESET)
    time.sleep(2)
    print("아침에 일어나보니 "+x+"(이)가 어젯밤에 카톡을 보내놨습니다."+c.RESET)
    time.sleep(2)
    print(x+":집에 잘 도착했어??"+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"뭐라고 답장해야 할까요?"+c.RESET)
    time.sleep(2)
    sentence=input("답장을 입력하세요:"+c.RESET)
    time.sleep(2)
    if check_word(sentence, target_word):
        print(c.CYAN+"호감도가",random.randint(5,15),"% 올랐습니다."+c.RESET)
    else:
        print(c.CYAN+"호감도가",random.randint(1,10),"% 올랐습니다."+c.RESET)
    time.sleep(2)
    print(x+":나중에",apark+"에서 봐"+c.RESET)
    time.sleep(2)
    print("--몇 시간 후 약속한 시각이 다 되고--"+c.RESET)
    time.sleep(2)
    print(x+"(이)와 당신은 만났습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 놀이기구를 타야할까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:회전목마, 2:롤러코스터, 3:동물원, 4:귀신의 집"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        elif num==2:
            print(c.CYAN+"호감도가",random.randint(1,5),"% 올랐습니다."+c.RESET)
            break
        elif num==3:
            print(c.CYAN+"호감도가",random.randint(10,15),"% 올랐습니다."+c.RESET)
            break
        elif num==4:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        else:
            back()
    print("점심시간이 되었습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"무엇을 먹어야 할까요?"+c.RESET)
    time.sleep(2)
    option4()
    time.sleep(2)
    print(c.MAGENTA+"1:닭강정, 2:핫도그, 3:햄버거, 4:회오리 감자, 추로스"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            print(c.CYAN+"호감도가",random.randint(10,15),"% 올랐습니다."+c.RESET)
            break
        elif num==2:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        elif num==3:
            print(x+"(이)는 햄버거가 손에 묻어 싫어합니다.")
            print(c.CYAN+"호감도가",random.randint(10,20)*-1,"% 감소했습니다."+c.RESET)
            neg(likability)
            break
        elif num==4:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        else:
            back()

    print("배를 다 채웠습니다."+c.RESET)
    time.sleep(2)
    print("지금 게임 부스로 왔습니다."+c.RESET)
    time.sleep(2)
    print(c.UNDERLINE +"어떤 게임을 할 것인가요?"+c.RESET)
    time.sleep(2)
    option3()
    time.sleep(2)
    print(c.MAGENTA+"1:사격게임, 2:농구 게임, 3:인형 뽑기"+c.RESET)
    time.sleep(2)
    num=int(input())
    while 1:
        if num==1:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        elif num==2:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        elif num==3:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        else:
            back()
    print("게임을 다했습니다."+c.RESET)
    time.sleep(2)
    print("인생네컷을 찍으러 갈 것입니다."+c.RESET)
    time.sleep(2)
    print("인생네컷에 도착했습니다."+c.RESET)
    time.sleep(2)
    print("당신은 ",c.UNDERLINE +x,"(이)와 어떤 컨셉으로 사진을 찍을 건가요?"+c.RESET)
    time.sleep(2)
    option3()
    time.sleep(2)
    print(c.MAGENTA+"1:소품 쓰지 않고 흑백, 2:쥬디&닉, 3:여러 가지 소품들로 찍기"+c.RESET)
    num=int(input())
    while 1:
        if num==1:
            print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
            break
        elif num==2:
            print(c.CYAN+"호감도가",random.randint(15,20),"% 올랐습니다."+c.RESET)
            break
        elif num==3:
            print(c.CYAN+"호감도가",random.randint(1,5),"% 올랐습니다."+c.RESET)
            break
        else:
            back()
    print("사진 2장이 나왔습니다."+c.RESET)
    time.sleep(2)
    print(x+"(이)가 사진을 매우 마음에 들어 합니다."+c.RESET)
    time.sleep(2)
    print(c.CYAN+"호감도가",random.randint(5,10),"% 올랐습니다."+c.RESET)
    time.sleep(2)
    print("어느덧 놀다 보니 벌써 밥을 먹을 시간이 되었습니다."+c.RESET)
    time.sleep(2)
    print("예약한 애슐리로 가서 밥을 다 먹었습니다."+c.RESET)
    time.sleep(2)
    print("어느덧 해어질 시간입니다."+c.RESET)
    time.sleep(3)
    print("과연 호감도는 얼마일까요?"+c.RESET)
    time.sleep(2)
    print("3초 후에 공개됩니다."+c.RESET)
    time.sleep(1)
    print("==========---3---=========="+c.RESET)
    time.sleep(1)
    print("==========---2---=========="+c.RESET)
    time.sleep(1)
    print("==========---1---=========="+c.RESET)
    time.sleep(1)
    #최종 호감도 출력
    print(c.RED +x, "(이)가 당신에 대한 호감도는 " + c.RESET + b.RED + c.WHITE + "%d 입니다." % likability + c.RESET)

    # 호감도 값 전달하여 neg() 함수 호출
    neg(likability)

    # 호감도 데이터 저장
    likability_data[name] = likability
    save_data(likability_data)

    with open("top.txt", "a", encoding="utf-8") as f:
        f.write(str(likability) + " " + name + "\n")

    with open("top.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
        content = [line.strip().split(" ") for line in content]

    return content  # content 변수를 반환


# 게임이 끝난후 순위 보주는 코드
if __name__ == "__main__":
    content = start_program()  # content 변수에 반환 값을 할당

    show_ranking = input("순위를 보시겠습니까? (예/아니오): ")
    if show_ranking.lower() == "예":
        sorted_content = sorted(content, key=lambda x: int(x[0]), reverse=True)
        for index, item in enumerate(sorted_content):
                print("(%d)" % (index + 1), item[0], item[1])

    print("게임을 종료합니다.")