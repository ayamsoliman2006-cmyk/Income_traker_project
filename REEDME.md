# 💰 Personal Income & Expense Tracker

A simple and interactive Python application designed to help users manage their monthly finances, track fixed expenses, automatically calculate savings/investments, and view their remaining entertainment budget.

---

## 📝 Project Concept

Managing personal finances can be overwhelming. This project was built to solve that problem by taking a user's monthly income and primary spending categories, then automatically processing the breakdown:

1. **Fixed Expenses Tracking:** Tracks essential monthly costs like Rent, Utilities, Food & Groceries, Transportation, and Personal Care/Clothes.
2. **Automated Investment Plan:** Automatically allocates a fixed percentage (10%) of total income toward savings/investments.
3. **Remaining Budget Calculation:** Calculates the leftover money available for discretionary spending (Entertainment).
4. **Data Persistence & Visualization:** Saves all entries to a local CSV file and presents financial allocations using an intuitive Pie Chart.

---

## 🛠️ Architecture & Concepts

The project uses modular Python code following **Object-Oriented Programming (OOP)** principles:

* **`calculate.py` (`IncomeTracker` Class):** Handles the core financial mathematical calculations and data formatting.
* **`storage.py` (`DataStorage` Class):** Manages file I/O operations, ensuring data is saved to and retrieved from `income_tracker.csv`.
* **`app.py`:** Built with **Streamlit** for the frontend user interface and **Matplotlib** for data visualization.

---

## 🚀 How to Run the App

Follow these steps to set up and run the application on your local machine:

### 1. Install Required Libraries
Open your terminal or command prompt in the project folder and run:

pip install streamlit pandas matplotlib
2. Launch the Application
Run the Streamlit application using:
streamlit run app.py
or python -m streamlit run app.py
3. Open in Browser
If your browser does not open automatically, copy and paste the provided local URL (usually http://localhost:8501) into your web browser.
