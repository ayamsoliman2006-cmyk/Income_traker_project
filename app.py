import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from calculate import Income_traker
from data_tracker import Data

st.set_page_config(
    page_title="Personal Income & Expense Tracker",
    page_icon="💰",
    layout="wide",)

st.title("💰 Personal Income & Expense Tracker")
st.caption("Manage your monthly income, fixed expenses, investments, and remaining"
    " entertainment budget.")
st.markdown("---")

storage = Data()

# 4. تقسيم الشاشة إلى عمودين متجاورين (اليمين للبيانات واليسار للنتائج)
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
  st.subheader("📝 Enter Financial Details")

  with st.form("income_form"):
    in_col1, in_col2 = st.columns(2)

    with in_col1:
      monthly_income = st.number_input(
          "Monthly Income ($)", min_value=0.0, step=100.0, value=1000.0
      )
      rent = st.number_input(
          "Rent ($)", min_value=0.0, step=50.0, value=300.0
      )
      utilities = st.number_input(
          "Utilities ($)", min_value=0.0, step=10.0, value=50.0
      )
      food = st.number_input(
          "Food & Groceries ($)", min_value=0.0, step=50.0, value=150.0
      )

    with in_col2:
      transport = st.number_input(
          "Transportation ($)", min_value=0.0, step=10.0, value=50.0
      )
      clothes_skincare = st.number_input(
          "Clothes & Skincare ($)", min_value=0.0, step=10.0, value=100.0
      )

    submit_btn = st.form_submit_button("Calculate & Save Data")

  if submit_btn:
    tracker = Income_traker(monthly_income=monthly_income,
        rent=rent,
        utilities=utilities,
        food=food,
        clothes_skincare=clothes_skincare,
        transport=transport,)
    storage.save_data(tracker.all_data())
    st.success("Data saved successfully!")

with col2:
  history_df = storage.get_history()

  if not history_df.empty:
    latest = history_df.iloc[-1]

    st.subheader("📊 Current Summary")
    st.caption(f"Last Updated Date: {latest['date']}")

    # تجهيز الجدول
    summary_data = {
        "Category": [
            "Monthly Income",
            "Rent",
            "Utilities",
            "Food",
            "Transportation",
            "Clothes & Care",
            "Investment (20%)",
            "Remaining Entertainment",
        ],
        "Amount ($)": [
            f"${latest['monthly_income']:,.2f}",
            f"${latest['rent']:,.2f}",
            f"${latest['utilities']:,.2f}",

            f"${latest['food']:,.2f}",
            f"${latest['transport']:,.2f}",
            f"${latest['clothes_skincare']:,.2f}",
            f"${latest['investment']:,.2f}",
            f"${latest['entertainment']:,.2f}",
        ],
    }

    summary_df = pd.DataFrame(summary_data)

    # عرض الجدول
    st.table(summary_df)

    # رسم بياني مصغر لتمثيل التوزيع
    labels = [
        "Rent",
        "Utilities",
        "Food",
        "Transport",
        "Clothes",
        "Investment",
        "Entertainment",
    ]
    values = [
        latest["rent"],
        latest["utilities"],
        latest["food"],
        latest["transport"],
        latest["clothes_skincare"],
        latest["investment"],
        latest["entertainment"],
    ]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    st.pyplot(fig)
