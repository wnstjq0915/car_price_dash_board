import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    if st.checkbox('데이터 프레임 보기'): # 체크박스 선택하면 보여주기
        st.dataframe(df)

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대 / 최소 데이터 확인하기')
    column = st.selectbox('컬럼을 선택하세요.', df.columns[3:])
    st.text('최대 데이터')
    st.dataframe(df[df[column] == df[column].max()])
    st.text('최소 데이터')
    st.dataframe(df[df[column] == df[column].min()])

    st.subheader('컬럼 별 히스토그램')
    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', df.columns[4:])
    bins = st.number_input('빈의 갯수를 입력하세요. (10 ~ 30)', 10, 30, value=20)
    # bins를 슬라이더바로 하면 더 나을듯.
    # bins = st.slider('빈의 갯수를 입력하세요. (10 ~ 30)', min_value=10, max_value=30, value=20)

    fig = plt.figure()
    df[column].hist(bins=bins)

    plt.title(column + ' Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.pyplot(fig) # 그래프 그리기

    st.subheader('상관 관계 분석')

    column_list = st.multiselect('상관분석 하고싶은 컬럼을 선택하세요.', df.columns[3:])

    if len(column_list) >= 2: # 선택을 안하거나 하나만 선택하면 X
        fig2 = plt.figure() # 히트맵
        sns.heatmap(data=df[column_list].corr(), annot=True, vmin=-1, vmax=1, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        st.pyplot(fig2)