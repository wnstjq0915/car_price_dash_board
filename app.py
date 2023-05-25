import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('자동차 가격 예측 앱')

    menu = ['Home', 'EDA', 'ML']


    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0]:
        from app_home import fun_app_home
        fun_app_home()
    elif choice == menu[1]:
        from app_eda import run_app_eda
        run_app_eda()
    else:
        from app_ml import run_app_ml
        run_app_ml()

if __name__ == '__main__':
    main()