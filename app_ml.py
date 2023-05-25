import streamlit as st
import numpy as np
import joblib

def num_comma(x):
    x_num = list(str(x))
    comma = 0
    if len(x_num) // 3 > 0:
        comma += len(x_num) // 3
        if len(x_num) % 3 == 0:
            comma -= 1
    for i in range(comma):
        x_num.insert(-3 * (i + 1) - i, ',')
    return ''.join(x_num)


def run_app_ml():
    st.subheader('자동차 금액 예측')

    # 성별, 나이, 연봉, 카드빚, 자산을
    # 유저한테 입력받는다.

    gender = st.radio('성별 선택', ['남자', '여자'])
    if gender == '남자':
        gender = 0
    else:
        gender = 1

    age = st.number_input('나이 입력', 18, 100)

    salary = st.number_input('연봉 입력', 5000, 100000)

    debt = st.number_input('카드빚', 0, 10000000)

    worth = st.number_input('자산 입력', 1000, 10000000)


    # 버튼을 누르면 예측한 금액을 표시한다.

    if st.button('금액 예측'):

        new_data = np.array([gender, age, salary, debt, worth])
        new_data = new_data.reshape(1, 5)

        regressor = joblib.load('model/regressor.pkl')

        y_pred = regressor.predict(new_data)
        st.text(f'{num_comma(int(y_pred[0]))}달러 차량 구매 가능합니다.') # , 붙이는 것도 해보기.