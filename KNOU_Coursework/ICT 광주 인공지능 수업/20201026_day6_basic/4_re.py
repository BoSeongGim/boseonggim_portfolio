
#1.금액  입력
coin = int(input("금액을 입력하세여.(최대금액 10000원)"))

#1.2. 최대금액 초과 
if coin >=10000 :
    print("최대 금액을 초과하였습니다.")
    print("10000원만 적용되며, 초과금액은 반환됩니다.")
    coin = 10000
    
print("입금액 : ",coin)
    
#1.3. 음료 설명
print("음료 설명"); print("1-사이다 700원"); print("2-콜라 600원"); print("3-오렌지쥬스 800원")

#2.음료 선택
choice = int(input("음료번호 : ") )


#1.1. 금액 부족한 경우 & 3.잔액 출력
if choice == 1 :
    if coin >= 700 :
        print("사이다 나왔습니다. 잔액:",coin-700)
    else :
        print("실시않음. 잔액:",coin)

if choice == 2 : 
    if coin >= 600:
        print("콜라 나왔습니다. 잔액:",coin-600)
    else :
        print("실시않음. 잔액:",coin)
        
elif choice ==3 : 
    if coin >=800 :
        print("오렌지쥬스 나왔습니다. 잔액:",coin-800)
    else :
        print("실시않음. 잔액:",coin)
print("자판기 종료입니다.")
    
#모범답안
#nData = int(input('금액을 입력하세요'))
#nSel = int(input('선텍'))

#if(nData > 
