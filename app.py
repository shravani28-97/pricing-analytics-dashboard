import streamlit as st

st.title("Fixed Income & Derivatives Pricing Dashboard")

bond_yield = st.slider("10-Year Bond Yield (%)", 1.0, 5.0, 3.5)
bond_price = 1000 / (1 + bond_yield / 100)  # Simplified bond price calculation

st.write(f"📈 **Estimated Bond Price:** ${round(bond_price, 2)}")

S = st.slider("Bond Price ($)", 900, 1100, 1000)
X = st.slider("Strike Price ($)", 900, 1100, 1020)
option_price = max(0, S - X)  # Simplified option pricing

st.write(f"💰 **Estimated Call Option Price:** ${round(option_price, 2)}")
