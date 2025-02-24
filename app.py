import streamlit as st
import plotly.express as px
import pandas as pd

# 샘플 데이터 생성
payment_data = pd.DataFrame({
    'Payment Method': ['카드', '계좌이체', '휴대폰 결제', '간편결제', '기타'],
    'Usage (%)': [40, 25, 20, 10, 5]
})

review_data = pd.DataFrame({
    'Category': ['상품 수', '리뷰 수', '평균 평점'],
    'Count': [50000, 120000, 4.5]
})

# Streamlit 앱 레이아웃
st.title("에이블리 기반 자사몰 대시보드")

st.header("📌 결제수단 사용 비율")
fig1 = px.pie(payment_data, values='Usage (%)', names='Payment Method', title='결제수단 사용 비율')
st.plotly_chart(fig1)

st.header("📌 에이블리 리뷰 & 상품 연동 데이터")
fig2 = px.bar(review_data, x='Category', y='Count', title='리뷰 및 상품 데이터', text_auto=True)
st.plotly_chart(fig2)

st.header("📌 결제 수수료 비교")
fee_data = pd.DataFrame({'Platform': ['자사몰', '기존 플랫폼'], 'Fee (%)': [2.5, 10]})
fig3 = px.bar(fee_data, x='Platform', y='Fee (%)', text_auto=True, title='결제 수수료 비교')
st.plotly_chart(fig3)

st.write("### 쉽게 자사몰을 구축하고, 글로벌 확장까지 경험해보세요!")

# Streamlit 실행 명령: streamlit run app.py
