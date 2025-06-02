import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Model Validator", layout="wide")
st.title("📊 AI Model Validation Report")

file_path = "reports/report.csv"

if not os.path.exists(file_path):
    st.warning("No report found. Please run tests first.")
else:
    df = pd.read_csv(file_path)

    st.markdown("### ✅ Test Results")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    total = len(df)
    passed = df['correctness'].sum()
    failed = total - passed

    st.markdown(f"- ✅ Passed: **{passed}**")
    st.markdown(f"- ❌ Failed: **{failed}**")
