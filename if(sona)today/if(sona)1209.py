# 네이버 주식에서 카카오 현재 시세알아보고
# 뉴스기사 2페이지정도 긁어 오기

import requests
from bs4 import BeautifulSoup

st_url = "https://finance.naver.com/item/sise.naver?code=035720"
st_response = requests.get(st_url)
st_html = st_response.text
st_soup = BeautifulSoup(st_html,'html.parser')
st_price = st_soup.select_one("#_nowVal") #id값 / 한개

print('현재 카카오 시세는!!!!! '+st_price.text)

print('''
      =============================
          카카오 뉴스 기사로는!!!!
      =============================
      ''')

#start 파라미터 - 1페이지 1/ 2페이지 11/ 3페이지 21
page_num= 1
cnt= 1

for _ in range(2): #2페이지만
    print(f'<<<{page_num}페이지 뉴스기사>>>')
    ns_url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%B9%B4%EC%B9%B4%EC%98%A4&&start={cnt}"
    ns_response =  requests.get(ns_url)
    ns_html = ns_response.text
    ns_soup = BeautifulSoup (ns_html, 'html.parser')
    links = ns_soup.select(".news_tit") #클래스 값/ 여러개
    cnt += 10
    
    for news in links: #select는 리스트로 받아와지니까 반복문돌리기
        title= news.text
        url= news.attrs['href']
        print(title, url)
    page_num+=1