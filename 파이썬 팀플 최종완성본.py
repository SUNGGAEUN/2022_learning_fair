v1=""
v2=""
v3=""
v4=""
def replay1():
    global v3
    v3=""
    print("[동물,식물,나라,직업]중에서 하나를 선택해주세요")
    v3=input(':')
    문제시작함수()
def replay2():
    global v3
    v3=""
    print("[음식,식물,나라,직업]중에서 하나를 선택해주세요")
    v3=input(':')
    문제시작함수()
def replay3():
    global v3
    v3=""
    print("[,음식,동물,나라,직업]중에서 하나를 선택해주세요")
    v3=input(':')
    문제시작함수()
def replay4():
    global v3
    v3=""
    print("[음식,동물,식물,직업]중에서 하나를 선택해주세요")
    v3=input(':')
    문제시작함수()
def replay5():
    global v3
    v3=""
    print("[음식,동물,식물,나라]중에서 하나를 선택해주세요")
    v3=input(':')
    문제시작함수()
    
    
    
def 시작():
    print("스무고개 게임에 오신 여러분을 환영합니다. 게임을 진행하고 싶으면 '네'를 입력해주시고 아니면 '아니오'라고 입력해주십시오.")
    v1=input(':')
    if v1=='네':
        print('이 게임은 5개의 주제 중 한개를 선택하여 각 주제에서 주어진 제시어를 맞추는 게임입니다.')
        print()
        print('제시어를 맞출 수 있는 기회는 총 10번 주어집니다.')
        print()
        print('기본점수 100점으로 시작하며 한번 틀릴때 마다 10점씩 감점됩니다.')
        print()
        print('그럼 게임 시작하겠습니다.')
        print()
        print("[음식,동물,식물,나라,직업]중에서 하나를 선택해주세요")
        global v3
        v3=input(':')
    if v1=='아니오':
        print('정말로 하기 싫으신건가요?, 다시 한번만 생각해주세요...')
        print()
        print("지금이라도 다시 도전하고 싶으시면 '네' 아니면 '아니오'라고 입력해주세요")
        v2=input(':')
        if v2=='네':
            print('감사합니다! 주제 제시해 드리겠습니다')
            print()
            print("[음식,동물,식물,나라,직업]중에서 하나를 선택해주세요")
            v3=input(':')
        if v2=='아니오':
            print('알겠습니다.. 다음에 또 만나요!')
    
        

시작()


    
def 문제함수1():
    global v3
    global count
    if v3=='음식':
        count=10
        
    while count==10:
            print("양파와 파, 깻잎, 양배추와 같은 채소가 재료로 들어간다.")
            m=input("답:")
            print()
            if m=='떡볶이':
                print("정답! 100점입니다! 한번에 맞추시다니 대단하시네요.")
                break
            else:
                print('신중하게 생각해주세요 기회 9번 남았습니다!')
                print()
                print("가열해서 먹는 음식이다.")
                m=input("답:")
                print()
                if m=="떡볶이":
                    print("정답! 90점 입니다! .")
                    break
                else:
                    print('신중하게 생각해주세요 아직 기회 8번 남았습니다!')
                    print()
                    print("남녀노소 호불호가 적은 음식이다.")
                    m=input("답:")
                    print()
                    if m=="떡볶이":
                        print("정답! 80점입니다 .")
                        break
                    else:
                        print('신중하게 생각해주세요 아직 기회 7번 남았습니다!')
                        print()
                        print("달고 매운맛이 특징이다.")
                        m=input("답:")
                        print()
                        if m=="떡볶이":
                             print("정답! 70점입니다 .")
                             break
                        else:
                            print('신중하게 생각해주세요 아직 기회 6번 남았습니다!')
                            print()
                            print("다양한 응용버전이 존재한다.")
                            m=input("답:")
                            print()
                            if m=="떡볶이":
                                print("정답! 60점입니다")
                                break
                            else:
                                print('신중하게 생각해주세요 아직 기회 5번 남았습니다!')
                                print()
                                print("소세지,당면,어묵,계란등 다양한 재료와 어울린다.")
                                m=input("답:")
                                print()
                                if m=="떡볶이":
                                    print("정답! 50점입니다")
                                    break
                                else:
                                    print('신중하게 생각해주세요 아직 기회 4번 남았습니다!')
                                    print()
                                    print("떡이 재료로 들어간다.")
                                    m=input("답:")
                                    print()
                                    if m=="떡볶이":
                                        print("정답! 40점입니다.")
                                        break
                                    else:
                                        print('신중하게 생각해주세요 이제  기회 3번 밖에  남았습니다!')
                                        print()
                                        print("치즈나 라면사리와 조합이 좋다.")
                                        m=input("답:")
                                        print()
                                        if m=="떡볶이":
                                            print("정답! 30점입니다.")
                                            break
                                        else:
                                            print('신중하게 생각해주세요 이제  기회 2번 밖에  남았습니다!')
                                            print()
                                            print("먹고 남은 국물에 볶음밥을 해먹기도한다.")
                                            m=input("답:")
                                            print()
                                            if m=="떡볶이":
                                                print("정답! 20점입니다.")
                                                break
                                            else:
                                                print('신중하게 생각해주세요 이제 마지막 기회입니다!')
                                                print()
                                                print("10대들에 인기가 많은 엽기OOO의 대표메뉴이다.")
                                                m=input("답:")
                                                print()
                                                if m=="떡볶이":
                                                    print("정답! 10점입니다.")
                                                    break
                                                if m!="떡볶이":
                                                    print("아쉽지만 기회 내에 정답을 맞추지 못하셨네요.")
                                                    print("다음에는 맞추시길 바랄게요!")
                                                    break
    print()
    print('재미있으셨나요? 다른 주제도 도전해보시겠어요?')
    print()
    print("다른 주제 선택하시려면 '네' 아니면 '아니오'라고 입력해주세요.")
    print()
    replay=input(':')
    if replay=='네':
        replay1()
        
    else:
        print('알겠습니다! 게임을 플레이 해주셔서 감사합니다!')
        print()
        print('좋은 하루 되세요~!')
        
def 문제함수2():
    global v3
    global count
    if v3=='동물':
        count=10
        
    while count==10:
            print("개과 동물이다.")
            m=input("답:")
            print()
            if m=='너구리':
                print("정답! 100점입니다! 한번에 맞추시다니 대단하시네요.")
                break
            else:
                print('신중하게 생각해주세요 기회 9번 남았습니다!')
                print()
                print("몸길이 평균 50~68cm에 무게는 4~10kg이다.")
                m=input("답:")
                print()
                if m=="너구리":
                    print("정답! 90점 입니다! .")
                    break
                else:
                    print('신중하게 생각해주세요 아직 기회 8번 남았습니다!')
                    print()
                    print("수명은7~10년이다.")
                    m=input("답:")
                    print()
                    if m=="너구리":
                        print("정답! 80점입니다 .")
                        break
                    else:
                        print('신중하게 생각해주세요 아직 기회 7번 남았습니다!')
                        print()
                        print("분포 지역은 유럽과 동아시아에 걸쳐 분포한다.")
                        m=input("답:")
                        print()
                        if m=="너구리":
                             print("정답! 70점입니다 .")
                             break
                        else:
                            print('신중하게 생각해주세요 아직 기회 6번 남았습니다!')
                            print()
                            print("네 다리는 짧고 꼬리는 굵다.")
                            m=input("답:")
                            print()
                            if m=="너구리":
                                print("정답! 60점입니다")
                                break
                            else:
                                print('신중하게 생각해주세요 아직 기회 5번 남았습니다!')
                                print()
                                print("잡식성 동물이다.")
                                m=input("답:")
                                print()
                                if m=="너구리":
                                    print("정답! 50점입니다")
                                    break
                                else:
                                    print('신중하게 생각해주세요 아직 기회 4번 남았습니다!')
                                    print()
                                    print("겨울잠을 자는 동물중 하나이다.")
                                    m=input("답:")
                                    print()
                                    if m=="너구리":
                                        print("정답! 40점입니다.")
                                        break
                                    else:
                                        print('신중하게 생각해주세요 이제  기회 3번 밖에  남았습니다!')
                                        print()
                                        print("긴털을 가지고 있으며 전채적으로 검은 털과 갈색털을 가지고있다.")
                                        m=input("답:")
                                        print()
                                        if m=="너구리":
                                            print("정답! 30점입니다.")
                                            break
                                        else:
                                            print('신중하게 생각해주세요 이제  기회 2번 밖에  남았습니다!')
                                            print()
                                            print("음식을 씻어먹는 라쿤과 친척관계이다.")
                                            m=input("답:")
                                            print()
                                            if m=="너구리":
                                                print("정답! 20점입니다.")
                                                break
                                            else:
                                                print('신중하게 생각해주세요 이제 마지막 기회입니다!')
                                                print()
                                                print("유명 라면 회사의 라면 중 하나이다.")
                                                m=input("답:")
                                                print()
                                                if m=="너구리":
                                                    print("정답! 10점입니다.")
                                                    break
                                                if m!="너구리":
                                                    print("아쉽지만 기회 내에 정답을 맞추지 못하셨네요.")
                                                    print("다음에는 맞추시길 바랄게요!")
                                                    break
    print('재미있으셨나요? 다른 주제도 도전해보시겠어요?')
    print()
    print("다른 주제 선택하시려면 '네' 아니면 '아니오'라고 입력해주세요.")
    print()
    replay=input(':')
    if replay=='네':
        replay2()
    else:
        print('알겠습니다! 게임을 플레이 해주셔서 감사합니다!')
        print()
        print('좋은 하루 되세요~!')
def 문제함수3():
    global v3
    global count
    if v3=='식물':
        count=10
        
    while count==10:
            print("나무에 피는 꽃이다.")
            m=input("답:")
            print()
            if m=='매화':
                print("정답! 100점입니다! 한번에 맞추시다니 대단하시네요.")
                break
            else:
                print('신중하게 생각해주세요 기회 9번 남았습니다!')
                print()
                print("나무의 높이가 5~10m가량하는 나무에 피는 꽃이다.")
                m=input("답:")
                print()
                if m=="매화":
                    print("정답! 90점 입니다! .")
                    break
                else:
                    print('신중하게 생각해주세요 아직 기회 8번 남았습니다!')
                    print()
                    print("분포지역은 한국 일본 중국에 걸쳐 분포한다.")
                    m=input("답:")
                    print()
                    if m=="매화":
                        print("정답! 80점입니다 .")
                        break
                    else:
                        print('신중하게 생각해주세요 아직 기회 7번 남았습니다!')
                        print()
                        print("꽃의 색깔은 흰색,붉은색,분홍색,연두색으로 다양하다.")
                        m=input("답:")
                        print()
                        if m=="매화":
                             print("정답! 70점입니다 .")
                             break
                        else:
                            print('신중하게 생각해주세요 아직 기회 6번 남았습니다!')
                            print()
                            print("개화시기는 1~4월정도이다.")
                            m=input("답:")
                            print()
                            if m=="매화":
                                print("정답! 60점입니다")
                                break
                            else:
                                print('신중하게 생각해주세요 아직 기회 5번 남았습니다!')
                                print()
                                print("꽃말은 고격과 기품이다.")
                                m=input("답:")
                                print()
                                if m=="매화":
                                    print("정답! 50점입니다")
                                    break
                                else:
                                    print('신중하게 생각해주세요 아직 기회 4번 남았습니다!')
                                    print()
                                    print("조선시대 묵화에 자주 등장한 꽃이다.")
                                    m=input("답:")
                                    print()
                                    if m=="매화":
                                        print("정답! 40점입니다.")
                                        break
                                    else:
                                        print('신중하게 생각해주세요 이제  기회 3번 밖에  남았습니다!')
                                        print()
                                        print("이 꽃의 열매는 매실이다.")
                                        m=input("답:")
                                        print()
                                        if m=="매화":
                                            print("정답! 30점입니다.")
                                            break
                                        else:
                                            print('신중하게 생각해주세요 이제  기회 2번 밖에  남았습니다!')
                                            print()
                                            print("생김새가 유사한 벚꽃과 혼동되기도한다.")
                                            m=input("답:")
                                            print()
                                            if m=="매화":
                                                print("정답! 20점입니다.")
                                                break
                                            else:
                                                print('신중하게 생각해주세요 이제 마지막 기회입니다!')
                                                print()
                                                print("상명대학교 교화이다.")
                                                m=input("답:")
                                                print()
                                                if m=="매화":
                                                    print("정답! 10점입니다.")
                                                    break
                                                if m!="매화":
                                                    print("아쉽지만 기회 내에 정답을 맞추지 못하셨네요.")
                                                    print("다음에는 맞추시길 바랄게요!")
                                                    break
    print('재미있으셨나요? 다른 주제도 도전해보시겠어요?')
    print()
    print("다른 주제 선택하시려면 '네' 아니면 '아니오'라고 입력해주세요.")
    print()
    replay=input(':')
    if replay=='네':
        replay3()
    else:
        print('알겠습니다! 게임을 플레이 해주셔서 감사합니다!')
        print()
        print('좋은 하루 되세요~!')
def 문제함수4():
    global v3
    global count
    if v3=='나라':
        count=10
        
    while count==10:
            print("날씨가 고온다습하다.")
            m=input("답:")
            print()
            if m=='브라질':
                print("정답! 100점입니다! 한번에 맞추시다니 대단하시네요.")
                break
            else:
                print('신중하게 생각해주세요 기회 9번 남았습니다!')
                print()
                print("다양한 인종이 모여있는 나라이다.")
                m=input("답:")
                print()
                if m=="브라질":
                    print("정답! 90점 입니다! .")
                    break
                else:
                    print('신중하게 생각해주세요 아직 기회 8번 남았습니다!')
                    print()
                    print("과거에 식민지배를 당했던 나라이다.")
                    m=input("답:")
                    print()
                    if m=="브라질":
                        print("정답! 80점입니다 .")
                        break
                    else:
                        print('신중하게 생각해주세요 아직 기회 7번 남았습니다!')
                        print()
                        print("포르투갈어를 사용한다.")
                        m=input("답:")
                        print()
                        if m=="브라질":
                             print("정답! 70점입니다 .")
                             break
                        else:
                            print('신중하게 생각해주세요 아직 기회 6번 남았습니다!')
                            print()
                            print("월드컵이 개최되었던 나라이다.")
                            m=input("답:")
                            print()
                            if m=="브라질":
                                print("정답! 60점입니다")
                                break
                            else:
                                print('신중하게 생각해주세요 아직 기회 5번 남았습니다!')
                                print()
                                print("남아메리카에 위치한 나라이다.")
                                m=input("답:")
                                print()
                                if m=="브라질":
                                    print("정답! 50점입니다")
                                    break
                                else:
                                    print('신중하게 생각해주세요 아직 기회 4번 남았습니다!')
                                    print()
                                    print("전통적인 춤이 유명한 나라이다.")
                                    m=input("답:")
                                    print()
                                    if m=="브라질":
                                        print("정답! 40점입니다.")
                                        break
                                    else:
                                        print('신중하게 생각해주세요 이제  기회 3번 밖에  남았습니다!')
                                        print()
                                        print("축구 강국중 하나이다.")
                                        m=input("답:")
                                        print()
                                        if m=="브라질":
                                            print("정답! 30점입니다.")
                                            break
                                        else:
                                            print('신중하게 생각해주세요 이제  기회 2번 밖에  남았습니다!')
                                            print()
                                            print("세계 7대 불가사의로 알려진 예수상이 존재하는 나라이다.")
                                            m=input("답:")
                                            print()
                                            if m=="브라질":
                                                print("정답! 20점입니다.")
                                                break
                                            else:
                                                print('신중하게 생각해주세요 이제 마지막 기회입니다!')
                                                print()
                                                print("지구의 허파라고 불리는 아마존이 있는 나라이다.")
                                                m=input("답:")
                                                print()
                                                if m=="브라질":
                                                    print("정답! 10점입니다.")
                                                    break
                                                if m!="브라질":
                                                    print("아쉽지만 기회 내에 정답을 맞추지 못하셨네요.")
                                                    print("다음에는 맞추시길 바랄게요!")
                                                    break

    print('재미있으셨나요? 다른 주제도 도전해보시겠어요?')
    print()
    print("다른 주제 선택하시려면 '네' 아니면 '아니오'라고 입력해주세요.")
    print()
    replay=input(':')
    if replay=='네':
        replay4()
    else:
        print('알겠습니다! 게임을 플레이 해주셔서 감사합니다!')
        print()
        print('좋은 하루 되세요~!')
def 문제함수5():
    global v3
    global count
    if v3=='직업':
        count=10
        
    while count==10:
            print("많은 사람들에게 도움이 되는 직업이다.")
            m=input("답:")
            print()
            if m=='간호사':
                print("정답! 100점입니다! 한번에 맞추시다니 대단하시네요.")
                break
            else:
                print('신중하게 생각해주세요 기회 9번 남았습니다!')
                print()
                print("최근 필요성이 대두되고있는 직업이다.")
                m=input("답:")
                print()
                if m=="간호사":
                    print("정답! 90점 입니다! .")
                    break
                else:
                    print('신중하게 생각해주세요 아직 기회 8번 남았습니다!')
                    print()
                    print("공부량이 방대한 직업중 하나이다.")
                    m=input("답:")
                    print()
                    if m=="간호사":
                        print("정답! 80점입니다 .")
                        break
                    else:
                        print('신중하게 생각해주세요 아직 기회 7번 남았습니다!')
                        print()
                        print("전문직종 중 하나인 직업이다.")
                        m=input("답:")
                        print()
                        if m=="간호사":
                             print("정답! 70점입니다 .")
                             break
                        else:
                            print('신중하게 생각해주세요 아직 기회 6번 남았습니다!')
                            print()
                            print("직업의 성비는 9:1로 여성의 성비가 높은 직업이다.")
                            m=input("답:")
                            print()
                            if m=="간호사":
                                print("정답! 60점입니다")
                                break
                            else:
                                print('신중하게 생각해주세요 아직 기회 5번 남았습니다!')
                                print()
                                print("국가고시를 통한 면허를 취득해야 활동할 수 있다.")
                                m=input("답:")
                                print()
                                if m=="간호사":
                                    print("정답! 50점입니다")
                                    break
                                else:
                                    print('신중하게 생각해주세요 아직 기회 4번 남았습니다!')
                                    print()
                                    print("환자를 치료하고 건강을 도모하는 일을 한다.")
                                    m=input("답:")
                                    print()
                                    if m=="간호사":
                                        print("정답! 40점입니다.")
                                        break
                                    else:
                                        print('신중하게 생각해주세요 이제  기회 3번 밖에  남았습니다!')
                                        print()
                                        print("우리나라 의료법상 의료인에 소속되어있다.")
                                        m=input("답:")
                                        print()
                                        if m=="간호사":
                                            print("정답! 30점입니다.")
                                            break
                                        else:
                                            print('신중하게 생각해주세요 이제  기회 2번 밖에  남았습니다!')
                                            print()
                                            print("나이팅게일이 이 직업의 대표 인물이다.")
                                            m=input("답:")
                                            print()
                                            if m=="간호사":
                                                print("정답! 20점입니다.")
                                                break
                                            else:
                                                print('신중하게 생각해주세요 이제 마지막 기회입니다!')
                                                print()
                                                print("병원에서 가장 많은 인원을 담당한다.")
                                                m=input("답:")
                                                print()
                                                if m=="간호사":
                                                    print("정답! 10점입니다.")
                                                    break
                                                if m!="간호사":
                                                    print("아쉽지만 기회 내에 정답을 맞추지 못하셨네요.")
                                                    print("다음에는 맞추시길 바랄게요!")
                                                    break

    print('재미있으셨나요? 다른 주제도 도전해보시겠어요?')
    print()
    print("다른 주제 선택하시려면 '네' 아니면 '아니오'라고 입력해주세요.")
    print()
    replay=input(':')
    if replay=='네':
        replay5()
    else:
        print('알겠습니다! 게임을 플레이 해주셔서 감사합니다!')
        print()
        print('좋은 하루 되세요~!')

def 문제시작함수():
    global v3
    if v3=='음식':
        문제함수1()
    elif v3=='동물':
        문제함수2()
    elif v3=='식물':
        문제함수3()
    elif v3=='나라':
        문제함수4()
    elif v3=='직업':
        문제함수5()
    
if v3=='음식':
    문제함수1()
elif v3=='동물':
    문제함수2()
elif v3=='식물':
    문제함수3()
elif v3=='나라':
    문제함수4()
elif v3=='직업':
    문제함수5()
    
    

    
                                                






