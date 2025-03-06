import streamlit as st
import datetime
import pyupbit
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

# 제목 작성이 가능하군..!
st.title('암호화폐 캔들 차트')

# 코인 리스트를 만들어 선택가능하게함
coin_list = [
    "KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-ADA", "KRW-DOGE", 
    "KRW-SOL", "KRW-DOT", "KRW-MATIC", "KRW-ATOM", "KRW-LINK",
    "KRW-BCH", "KRW-LTC", "KRW-AVAX", "KRW-NEAR", "KRW-ETC",
    "KRW-SAND", "KRW-AXS", "KRW-FTM", "KRW-MANA", "KRW-ZIL"] 
ticker = st.selectbox('코인 선택:', coin_list)

interval = 'minute60'

# 날짜 선택
d = st.date_input(
    "날짜를 선택하세요.",
    datetime.date.today())

to = str(d + datetime.timedelta(days=1))
count = 24
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

# 캔들차트
if price_now is not None:
    st.write(f'{ticker} 1시간봉 차트')
   
    # 데이터 변환
    price_now = price_now[['open', 'high', 'low', 'close', 'volume']]

    # matplotlib으로 캔들차트 생성
    fig, ax = plt.subplots(figsize=(10, 5))
    mpf.plot(price_now, type='candle', style='charles', ax=ax)

    st.pyplot(fig)
else:
    st.error("에러 발생")
