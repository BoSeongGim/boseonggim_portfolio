
'''
#딕셔너리 - 없는 값 로드시에는 에러남.
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72 }
#lux['attack_speed'] #에러예제

lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72 }
print('health' in lux)
print('attct_speed' in lux)

print('attact_speed' not in lux)
print('health' not in lux)


lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72 }
print(len(lux))
print(len({'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72 }))


camille = {
        'health' : 575.6,
        'health_regen' : 1.7,
        'mana' : 338.8,
        'mana_regen' : 1.63,
        'melee' : 125,
        'attack_damage' : 60,
        'attack_speed' : 0.625,
        'armor' : 26,
        'magic_resistance' : 32.1,
        'movement_speed' : 340
        }

print(camille['health'])
print(camille['movement_speed'])
'''

'''
in1 = input("키 이름 입력 : ").split() 
# in2 = input("값 입력 : ").split() #나의 코딩 NG/실수가 아니라 str형으로 입력받기 때문.
in2 = map(float, input("값 입력 : ").split() ) #실수로 입력 받기 위함.
#map(float, input("값 입력 : ").split() )
#mapping한다(실수형으로, 입력한다.여러개 입력시 설정 

#map에서 '(float' 미선언시에는 str으로 입력 받음.

print(in1)
print(type(in1))

print(in2)
print(type(in2))

lux2 = dict(zip(in1, in2 ))
print("lux2 : ", lux2)
'''

'''
if 조건식 :
    코드 
'''

x = 10
if x ==10 :
    print('10입니다')
    print('10이랑께유!')
    print('ㅋㅋㅋㅋㅋㅋㅋㅋ')

if x != 10 : 
    print("ddddddd")




print("12456")

















