print("====상명대학교 신입생을 위한 정문 계단 길안내 로봇====")
print()
print("당신이 가고자 원하는 곳을 입력하세요!")
print()
print("1. 상록관 2. 계당관 3. 학생회관 4. 한누리관 5. 학생기숙사")
print()
destination=int(input('숫자로만 입력하세요: '))
if destination==1 :
    print("오! 상록관은 매우 가깝습니다. 함께 가볼까요?")
    print("우선 계단을 올라가 사슴상을 찾아보세요! 찾으셨나요?")
    print()
    answer=int(input("1.yes 2.no 대답은 숫자로 입력하십시오 "))
    if answer==2:
        while True:
            print("상명대의 사슴상은 올라타면 cc를 이룰 수 있다는 전설이 있어요. 생각보다 크지 않으니 왼편에서 잘 찾아보세요!")
            print()
            answer1 = int(input("찾으셨나요? 1.yes 2.no 대답은 숫자로 입력하십시오 "))
            if answer1 == 1:
                print()
                print("잘하셨습니다! 사슴상 뒤편으로 보이는 건물 중 오른쪽이 상록관 입니다ㅎㅎ")
                break
    else:
        print()
        print("잘하셨습니다! 사슴상 뒤편으로 보이는 건물 중 오른쪽이 상록관 입니다ㅎㅎ")

elif destination ==2:
    print("오! 계당관은 들끓는 피와 열정으로 가득찬 곳이죠! 같이 가 봅시다 ㅎㅎ")
    print()
    print("오른쪽을 쭉 보세요! Cu편의점이 보이시나요?")
    print()
    answer=int(input("1.yes 2.no 대답은 숫자로 입력하십시오 "))
    if answer==2:
        while True:
            print("바로 오른쪽을 보시면 학술정보관이 보일거에요. 그 사이에 있는 돌계단을 따라 나가다 보면 더 잘 보인답니다!")
            answer1 = int(input("찾으셨나요? 1.yes 2.no 대답은 숫자로 입력하십시오 "))
            if answer1 == 1:
                print("잘하셨습니다! Cu편의점이 있는 건물이 바로 계당관 입니다ㅎㅎ")
                break
    else:
        print("잘하셨습니다! Cu편의점이 있는 건물이 바로 계당관 입니다ㅎㅎ")

elif destination ==3:
    print("wow! 학생회관은 맛있는 학생식당과 동아리 방이 밀집한 곳이죠~ 거리가 좀 있으니 조심히 가봅시다!")
    print()

    input('한 번 화이팅 외쳐 볼까요?')
    print()
    print("좋습니다 먼저 계단을 쭉 올라가 분수를 찾아볼까요? 분수를 찾으셨나요?")
    print()
    answer=int(input("1.yes 2.no 대답은 숫자로 입력하십시오 "))
    if answer==2:
        while True:
            print("상명대의 트레이드 마크라고 할 수 있는 화려한 분수! 정면에 보이는 계단을 한 번 더 올라가면 더 잘 보일거에요!  ")
            answer=int(input('분수를 찾으셨나요? 1. 네 찾았어요! 2. 아뇨 아직입니다. '))
            if answer== 1:
                print()
                print("잘하셨습니다! 이제 오른쪽으로 돌아 무작정 직진해볼까요?")
                input()
                break
    else:
        print()
        print("잘하셨습니다! 이제 오른쪽으로 돌아 무작정 직진해볼까요? ")
        input()
        
    print("거의 다 왔습니다. 혹시 중간에 왼쪽에 보이는 계단으로 올라가신 건 아니죠?")
    print()
    answer=int(input("1.yes 2.no 대답은 숫자로 입력하십시오 "))
    if answer==2:
        while True:
            answer1=int(input("거기로 올라가면 안돼요! 어서 내려와주세요.  1.네.. 2.싫어요!"))
            if answer1 ==1:
                print()
                print("운동한 셈 칩시다! 이제 왼편으로 큰 오르막길이 나올 때까지 걸어가주세요.")
                print()
                break
    else:
        print()
        print("다행이네요! 왼편으로 큰 오르막길이 나올 때까지 걸어가주세요.")
        input('벌써 지치신건 아니죠?^^')
        print()
    print("왼쪽에 보이는 오르막길을 올라가다 보면 바로 오른쪽에 있는 건물이 학생회관이랍니다. 고생하셨어요 :)")

elif destination ==4:
    print('한누리관은 상명대학교 천안캠퍼스를 대표하는 랜드마크 건물입니다.')
    print("수업의 대부분이 한누리관에서 이루어지는 만큼 경로를 꼭 잘 알아두어야 한답니다~")
    print()
    print("오른쪽을 쭉 보세요! Cu편의점이 보이시나요?")
    answer=int(input("1.yes 2.no 대답은 숫자로 입력하십시오 "))
    if answer==2:
        while True:
            print("바로 오른쪽을 보시면 학술정보관이 보일거에요. 그 사이에 있는 돌계단을 따라 나가다 보면 더 잘 보인답니다!")
            answer1 = int(input("찾으셨나요? 1.yes 2.no 대답은 숫자로 입력하십시오 "))
            if answer1 == 1:
                print("잘하셨습니다!")
                print()
                break
    else:
        print("잘하셨습니다!")
        print()

    input('한 번 가보자고~! 를 외쳐 볼까요?')
    print()
    print("좋습니다. 이제 눈 앞에 보이는 언덕을 따라 쭉~ 올라가세요.")

    print("올라가셨다면 노천극장을 뒤로하고 눈 앞에 계단이 보이실 거에요 :)")
    print()
    print("한 번 뒤를 돌아서 노천극장을 바라보시겠어요? 노을과 함께라면 이만한 광경이 없답니다. 어때요, 황홀하지 않으신가요?")
    answer1=int(input("1.네 정말 이뻐요! 2.아니요 저는 그닥... 대답은 숫자로 입력하십시오 "))
    if answer1==2:
        while True:
            print("해가 질 때까지 노숙을 쳐 하시던가, 다시 한 번 깊이 생각해보세요~")
            print()
            answer2= int(input("이제 좀 이뻐보이나요? 1.네 진짜로요 2.NO. 대답은 숫자로 입력하십시오 "))
            if answer2==1:
                print("하하~ 보면 볼 수록 이쁜 것이 상명대학교의 특징이죠! 우리 학교는 자연환경이 참 잘 어우러진 아름다운 학교랍니다.")
                input('그쵸~~? <아무 말이나 하셔도 됩니다>')
                break
    else:
        print()
        print("보는 눈이 있으시네요! 이제 계단을 올라가시면 정면에 보이는 건물이 한누리관 입니다.")
        print()
    print("올라가시다보면 조형물이 하나 있는데, 이곳에서 '연플리' 라는 인기 웹드라마도 제작했답니다.")
    input('참 이쁘죠? <아무 말이나 하셔도 됩니다>')
    print()
    print("하하, 고생 많으셨습니다. 이제 한누리관에서  행복한 대학생활을 즐기시길 바랄게요!")



elif destination==5 :
    print("학교에서 가장 가까운 집, 학생기숙사로 안내합니다!")
    print("정문을 등지고 쭉 직진 하세요!! 작은 언덕 위 테니스장이 보이시나요?")

    print()
    answer=int(input("1.yes 2.no 대답은 숫자로 입력하십시오"))
    if answer==2:
        while True:
            print("계속 직진하다보면 옆에 학생들의 땀과 열정이 묻어있는 운동장과 농구장이 보일거에요. 그곳을 지나 앞에 있는 언덕위로 올라가 보세요!")
            print()
            answer1 = int(input("찾으셨나요? 1.yes 2.no 대답은 숫자로 입력하십시오 "))
            if answer1 == 1:
                print()
                print("좋아요! 상명 스포츠 센터와 테니스장 사이에 도착하니 운동을 하고 싶어지는데요? 좀만 더 걸어보자구요!")
                print("갈림길이 보일 때 까지 쭉 직진하세요! 갈림길의 가장 오른쪽 길로 들어오시면 건물이 두 개가 보이실 겁니다. 찾으셨나요?")
                print()
                answer2=int(input("1.yes 2.no 대답은 숫자로 입력하십시오"))
         
                if answer2==2:
                    while True:
                        print("갈림길의 오른쪽을 보면 마치 이탈리아의 피사의 사탑을 연상시키는 종합 실기관이 있습니다.")
                        print()
                        answer3 = int(input("보이시나요? 1.yes 2.no 대답은 숫자로 입력하십시오 "))
                        if answer3 == 1:
                            print()
                            print("잘하셨습니다! 종합 실기관 앞에 있는 건물이 바로 학생기숙사입니다. 계단을 올라간 뒤 건물 안으로 들어가세요!")

                            print("편안한 휴식 되세요, 감사합니다!")
                            break
            else:
                continue
            break
    else:
        print()
        print("좋아요! 상명 스포츠 센터와 테니스장 사이에 도착하니 운동을 하고 싶어지는데요? 좀만 더 걸어보자구요!")
        print("갈림길이 보일 때 까지 쭉 직진하세요! 갈림길의 가장 오른쪽 길로 들어오시면 건물이 두 개가 보이실 겁니다. 찾으셨나요?")
        print()
        answer2=int(input("1.yes 2.no 대답은 숫자로 입력하십시오"))
        if answer2==2:
            while True:
                print("갈림길의 오른쪽을 보면 마치 이탈리아의 피사의 사탑을 연상시키는 종합 실기관이 있습니다.")
                print()
                answer3 = int(input("보이시나요? 1.yes 2.no 대답은 숫자로 입력하십시오 "))
                if answer3 == 1:
                    print()
                    print("잘하셨습니다! 종합 실기관 앞에 있는 건물이 바로 학생기숙사입니다. 계단을 올라간 뒤 건물 안으로 들어가세요!")
                    print("편안한 휴식 되세요, 감사합니다!")
                    break

        else:
            print()
            print("잘하셨습니다! 종합 실기관 앞에 있는 건물이 바로 학생기숙사입니다. 계단을 올라간 뒤 건물 안으로 들어가세요!")
            print("편안한 휴식 되세요, 감사합니다!")
