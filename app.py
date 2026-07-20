%%writefile requirements.txt
streamlit
pandas
plotly
%%writefile app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="BetNaija Impact", page_icon="🇳🇬", layout="wide")

# Custom styling
st.markdown("""
<style>
    .main-header {font-size: 2.8rem; color: #FF4B4B; text-align: center;}
    .sub-header {font-size: 1.5rem; color: #1E88E5;}
</style>
""", unsafe_allow_html=True)

st.title("🇳🇬 BetNaija Impact")
st.markdown("**10-Year Analysis of Nigeria's Betting Industry (2016–2025)**")

# Data
@st.cache_data
def load_data():
    data = {
        'Year': list(range(2016, 2026)),
        'Market_Size_USD_Billion': [0.8, 1.0, 1.2, 1.5, 1.6, 1.8, 2.2, 2.7, 3.0, 3.63],
        'Active_Bettors_Million': [3, 4, 5, 8, 12, 18, 25, 35, 60, 60],
        'Tax_Revenue_NGN_Billion': [8, 10, 12, 25, 35, 48, 65, 85, 200, 220],
        'Problem_Gambling_Percent': [7.0, 7.5, 8.0, 9.0, 11.0, 12.0, 13.0, 14.0, 14.3, 15.0]
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

tab1, tab2, tab3, tab4 = st.tabs(["📈 Market Trends", "⚖️ Profits vs Harms", "📊 Deep Analysis", "💰 Smart Finance Simulator"])

with tab1:
    st.subheader("Betting Market Growth in Nigeria")
    fig1 = px.line(df, x='Year', y='Market_Size_USD_Billion', markers=True, 
                   title="Market Size (USD Billion)", color_discrete_sequence=["#FF4B4B"])
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Profits vs Harms")
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Economic Gains**")
        st.write("• Billions in tax revenue")
        st.write("• Jobs in tech & marketing")
    with col2:
        st.error("**Harms on Nigerians**")
        st.write("• Massive financial losses")
        st.write("• Addiction & mental health issues")
        st.write("• Youth debt and poor academics")
        st.write("• Money not invested in real businesses")

with tab3:
    st.subheader("10-Year Data")
    st.dataframe(df, use_container_width=True)

with tab4:
    st.subheader("Smart Finance Simulator")
    st.caption("See the real cost of betting")
    
    income = st.number_input("Your Monthly Income (₦)", min_value=30000, value=150000, step=5000)
    percent = st.slider("Percentage of Income on Betting (%)", 0, 100, 15)
    months = st.slider("How Many Months?", 1, 60, 12)
    
    monthly_bet = income * (percent / 100)
    total = monthly_bet * months
    loss = total * 0.85
    missed = total * 0.08 * (months / 12)
    
    st.success(f"Total Bet: **₦{total:,.0f}**")
    st.error(f"Estimated Loss: **₦{loss:,.0f}**")
    st.info(f"Missed Savings: **₦{missed:,.0f}**")
    
    if percent >= 30:
        st.error("🚨 This is very dangerous and can lead to serious debt.")

!streamlit run app.py --server.headless true --server.port 8501 & npx localtunnel --port 8501
