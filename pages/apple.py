import yfinance as yf
import streamlit as st
import pandas as pd


st.title('Данные о катировках компании Apple')
st.write('Выберете тип данных для отображения')
st.subheader('Выберите период данных')

start_date = st.date_input('Начальная дата', pd.to_datetime('2005-01-01'))
end_date = st.date_input('Конечная дата', pd.to_datetime('2022-01-01'))

data_box =  st.selectbox('Выберете тип данных', ['Close', 'Volume', 'High', 'Low'])

tiker_symbol = 'AAPL'

tiker_data = yf.Ticker(tiker_symbol)

tikerDF = tiker_data.history(period='1d', start='2005-01-01', end='2022-01-01')

if data_box == 'Close':
    st.line_chart(tikerDF['Close'])
elif data_box == 'Volume':
    st.line_chart(tikerDF['Volume'])
elif data_box == 'High':
    st.line_chart(tikerDF['High'])
elif data_box == 'Low':
    st.line_chart(tikerDF['Low'])   


st.subheader('Статистика по выбранным данным')
st.write(tikerDF[data_box].describe())        