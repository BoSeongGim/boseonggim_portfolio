lux = {'health':490, 'mana':334, 'melee' : 550, 'armor':18.72}
print("lux:",lux)

#딕셔너리 요소는 중복시 가장 뒤의 값만 쓰인다.
lux = {'health':490,'health':999, 'health':121213,'mana':334, 'melee' : 550, 'armor':18.72}
print(lux['health'])
print(lux)


#딕셔너리는 문자열/정수.실수.불,리스트 등 모두 섞어 쓸수 있다.
x = {100:'hundred', False:0, 3.5:[3.5, 3.5]}
print(x)


#값에는 리스트 불가인듯?
#빈 딕셔너리 생성하기 2가지 방법.
x={}
print(x)
y=dict()
print(y)

'''
딕셔너리 생성법
방법1) 딕셔너리명 = {'요소1'=값1, .... }
방법2) dict 사용, 4가지방법 있음.
'''

#키=값 형식으로 딕셔너리를 만든다.
#첫 번째 방법으로만 했음. 2번,3번 방법의 경우 잘 안쓰다고 하심.
lux1 = dict(health=490, mana=334, melee= 550, armor=18.72)

print("lux1:",lux1)

#zip합수로 만들기
lux2 = dict( zip(['health','mana','melee','armor']
                ,[490,334,550,18.72]) )
print("lux2 : ",lux2)

#(키,값) ㅅ형식의 튜플을 리스트 안에 넣기
lux3 = dict([('health',490), ('mana',334), ('melee',550), ('armor',18.72) ] )
print("lux3 : ",lux3)


#네번째 방법. 거의 안쓸듯....
lux4 = dict({'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72})
print("lux4 : ",lux4)

lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print("lux : ",lux['health'])
print("lux : ",['armor'])

#딕셔너리의 키의 값을 수정.
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux['health']=2038
lux['mana']=1184
print(lux)

#딕셔너리는 없는 키를 할당시 키가 추가됨(주의필요. 의도치 않은 값이 생성될 수 있어.) 
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux['mana_regen']=3.28
print(lux)




















