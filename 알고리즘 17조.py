print('<상명대학교 도서 시스템>')
code= input('로그인 단계입니다. 이름과 생년월일(YYMMDD)을 입력하세요.')
print('안녕하세요.', code + '님, 로그인 되셨습니다.')
print('\n')
answer = int(input('숫자를 입력하세요. 1) 대출하기 2) 반납하기:'))
print('\n')

if answer == 1:
    print('현재 대출 가능한 도서는 다음과 같습니다.')
    t = input('[생리학, 미생물학, 생명윤리, 인간성장과발달, 해부학, 간호학개론, 사회와건강]중 대출할 도서를 입력하세요.:')
    print(t + '를 대출하시겠습니까?')
    print('\n')
    
    답 = input('맞다면 Y를, 아니라면 N을 입력해주세요.:')
    if 답 == 'Y':
        print('\n')
        print('오늘 날짜(a월 b일)를 입력해주세요:')
        a= int(input('a:'))
        b= int(input('b:'))
        m = [4,6,9,11]
        g = b+7
        if a in m:
           if g > 30:
               a = a + 1
               b = g - 30
        elif a == 2:
            if g > 28:
                a = a + 1
                b = g -28
        else :
            if g > 31:
                a = a + 1
                b = g - 31
        if a > 12:
            a = 1
            
        print('반납예정일은', a, '월', b, '일', '까지 입니다.')
        print('대출 되셨습니다. 이용해주셔서 감사합니다.')

        if 답 == 'N':
            print('대출 취소되셨습니다. 이용해주셔서 감사합니다.')

else:
        response = int(input('반납하시겠습니까? 1)반납하기 2)취소:'))
        if response == 1:
            print('\n')
            print('대출하신 도서의 이름(name)과 대출일자(c월 d일)를 입력해주세요.')
            c = int(input('c:'))
            d = int(input('d:'))
            name= input('책이름:')
            print(c, '월', d , '일', '대출하셨던', name , '도서가 반납되셨습니다. 이용해주셔서 감사합니다.')

        if response == 2:
            print('\n')
            print('취소되셨습니다.')
