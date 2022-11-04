while True:
    choice = int(input('1. 주문하기 2. 종료하기 >> '))

    if choice == 2:
        print('다음에 또 오세요~')
        break

    elif choice == 1:
       stickCnt = 0
       sprinkleCnt = 0
       chocoCnt = 0
       penCnt = 0
       packCnt = 0

       while True:
           print('1. 막대과자 : 1500원')
           print('2. 스프링클 : 2500원')
           print('3. 화이트 초콜릿 : 2000원')
           print('4. 초코펜 : 1000원')
           print('5. 포장용 비닐 : 1500원')
           print('6. 결제하기')
           choice = int(input('>'))

           if choice == 1:
              stickCnt += 1
              print('막대과자 1개가 추가되었습니다.')
           elif choice == 2:
              sprinkleCnt += 1
              print('스프링클 1개가 추가되었습니다')
           elif choice == 3:
              chocoCnt += 1
              print('화이트 초콜릿 1개가 추가되었습니다.')
           elif choice == 4:
              penCnt += 1
              print('초코펜 1개가 추가되었습니다.')
           elif choice == 5:
              packCnt += 1
              print('포장용 비닐 1개가 추가되었습니다.')
           elif choice == 6: 
              price = stickCnt * 1500 + sprinkleCnt * 2500 + chocoCnt * 2000 + penCnt * 1000 + packCnt * 1500

              print('----내 주문 목록---')
              print('막대과자 :', stickCnt, '개')
              print('스프링클 :', sprinkleCnt, '개')
              print('화이트 초콜릿 :', chocoCnt, '개')
              print('초코펜 :', penCnt, '개')
              print('포장용 비닐 :', packCnt, '개')
              
              print('총 금액 :', price, '원')
              money = int(input('금액을 입력하시오 >> '))

              if money < price:
                  print('결제 실패! (잔액부족)')
                  break
              else:
                  print('결제 성공! 잔돈 :', money - price)
                  break

           else:
               print('잘못 입력했습니다.')

           print()

    else:
        print('다시 입력하시오.')

    print()
    
    
