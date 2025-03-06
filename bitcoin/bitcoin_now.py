import streamlit as st
import datetime
import pyupbit

# 제목 작성이 가능하군..!
st.title('암호화폐 실시칸 차트')

# 코인 리스트를 만들어 선택가능하게함
coin_list = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP', 'KRW-ADA', 'KRW-DOGE']
ticker = st.selectbox('코인 선택:', coin_list)

# 시간 간격을 선택가능하게함
interval_list = {
    '1분봉': 'minute1',
    '5분봉': 'minute5',
    '1시간봉': 'minute60'
}
interval_option = st.selectbox('봉(시간간격) 선택:', list(interval_list.keys()))
interval = interval_list[interval_option]

# 날짜 선택
d = st.date_input(
    "날짜를 선택하세요.",
    datetime.date.today())

to = str(d + datetime.timedelta(days=1))
count = 24 if interval == 'minute60' else 120
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

if price_now is not None:
    st.write(f'{ticker} {interval_option} 차트')
    st.line_chart(price_now.close)
else:
    st.error("에러 발생")