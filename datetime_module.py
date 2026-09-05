from datetime import datetime

today = datetime.now()
print('현재 날짜, 시각 데이터 today :', today)
print('today = datetime.now() :', today)
print('연, 월, 일 :', today.year,
today.month, today.day)
print('시, 분, 초 :', today.hour,
today.minute, today.second)
print('요일: ', today.weekday())
dday = datetime(2027, 6, 17, 0, 0, 0) # 2027년 뉴미디어IT쇼 날짜
print('지정한 d-day :', dday)
print('지나온 시간(today - dday): ', today - dday)