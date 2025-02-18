import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Fill in the blanks')
st.write('Upload your dataframe and fill in the blanks')

uploaded_file = st.sidebar.file_uploader('Upload a file CSV', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()

missing_values = df.isna().sum()
missing_values = missing_values[missing_values > 0]

if len(missing_values) > 0:
    fig, ax = plt.subplots()
    sns.barplot(x=missing_values.index, y=missing_values.values, ax=ax)
    ax.set_title('Missing values')
    ax.set_ylabel('Number of missing values')
    ax.set_xlabel('Columns')
    st.pyplot(fig)  

    if len(missing_values) != 0:
        button = st.button('Fill missing values')
        if button:
            df_filled = df[missing_values.index].copy() 
            for col in df_filled.columns:
                if df_filled[col].dtype == 'object':
                    df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
                else:
                    df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
            st.write(df_filled.head(5))


            st.download_button(label='Download filled dataset', data=df_filled.to_csv(), file_name='filled_dataset.csv', mime='text/csv')   

else:
    st.write('No missing values in the dataset')    
    st.stop()


