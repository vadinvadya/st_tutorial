import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Зависимость чаевых от стоимости заказа 🍽️💸')

file = st.sidebar.file_uploader('Загрузите данные о чаевых', type=['csv'])

 # Словарь для отображения пользовательских названий
column_names = {
    'Обед и ужин': 'lunch_dinner',
    'Обед': 'lunch',
    'Ужин': 'dinner',
}

    # Выбор пользовательского названия
selected_column = st.selectbox('Выберите тип данных', list(column_names.keys()))


if file is not None:
    if selected_column == 'Обед и ужин':
        tips = pd.read_csv(file)
        fig, ax = plt.subplots()
        sns.scatterplot(data=tips, x='total_bill', y='tip', style='time', hue='time')
        ax.set_title('Зависимость чаевых от стоимости заказа')
        st.pyplot(fig)
    elif selected_column == 'Обед':
        tips = pd.read_csv(file)
        tips = tips[tips['time'] != 'Dinner']
        fig, ax = plt.subplots()
        sns.scatterplot(data=tips, x='total_bill', y='tip')
        ax.set_title('Зависимость чаевых от стоимости заказаc (Обед)')
        st.pyplot(fig)
    elif selected_column == 'Ужин':
        tips = pd.read_csv(file)
        tips = tips[tips['time'] != 'Lunch']
        fig, ax = plt.subplots()
        sns.scatterplot(data=tips, x='total_bill', y='tip', marker='x', color='red')
        ax.set_title('Зависимость чаевых от стоимости заказа (Ужин)')
        st.pyplot(fig)      
        
else:
    st.stop()


st.subheader('Данные о чаевых')
st.dataframe(tips)
