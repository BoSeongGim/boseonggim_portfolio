#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python에서 HTTP 요청을 보내는 모듈
import requests
from bs4 import BeautifulSoup       #bs4라고 불리는 html 분석 라이브러리
import copy                         #
import threading                    #
from datetime import datetime      #시간관리하는 모듈

#스텝1 헤더,링크설정
#유저 설정(HTTP 헤더는 클라이언트와 서버가 요청 또는 응답으로 부가적인 정보를 전송할 수 있음.)
headers = {'User-Agent':'Mozila/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

#네이버 메인이 아닌 DataLab 페이지
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

#스텝2,카운트변수등 변수설정
nCount = 0 #n은 정수형을 의미.
outFp = open("n_real.txt","w",encoding='utf-8')

oldRtData = [None]*20 #20개의 단어들을 대상으로 함.
newRtData = [None]*20 #20개의 단어들을 대상으로 함.



#--ppt파트2------------------------------------------------------------
def readRTData() :
    #글로벌 선언하여 전역유지
    global oldRtData
    global newRtdata
    global nCount    #카운트는 들어올때마다 유지된다(리셋되지 않음.)
    
    for i in range(1,3):
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.content, 'html.parser')
        title_list = soup.select('span.item_title')

    for idx, title in enumerate(title_list,1):
        newRtData[idx-1] = title.text
        
    if newRtData == oldRtData :
        print('동일')
    else :
        print('변경')
        print(newRtData)
        for w_string in newRtData :
            print(w_string)
            now_T = datetime.now()
            outFp.writelines(str(now_T.hour)+'/'+str(now_T.minute) +'/'+str(now_T.second) + '/'+w_string + '/n')
        
        
#비교 후 기존 데이터를 새로운 데이터로 업데이트
oldRtData = copy.deepcopy(newRtData)
nCount +=1

if(nCount <200): #5초씩 200번 읽도록 설정시킴. 즉 5초마다 함수하도록 설정시킨 것.
    timer = threading.Timer(1,readRTData)
    timer.start()
else:
    outFp.close()
    print("=============종료======================")
        
        
readRTData()


# In[2]:


#조건1) 5초 간격으로 5분간의 실시간 검색어를 추적할 것.
#조건2) 실시간 검색어 결과가 기존과 다른 경우에 파일에 저장
#조건3) 저장할 때 몇 번째 확인인지를 표시하여 저장하세요
# 예. 시작후 5초면 1번째 확인, 55초후면 11번째 확인
#조건4)저장된 파일을 통하여 네이버 급상승 검색어 갱신 주기를 확인할 수 있음.


# In[ ]:





# In[ ]:





# In[ ]:




