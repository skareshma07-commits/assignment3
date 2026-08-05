import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
#                 EMPLOYEE PAYROLL DASHBOARD
# ---------------------------------------------------------

st.title("💼 Employee Payroll Dashboard")

# ---------------------------------------------------------
# Employee : Rahul Sharma
# Department : Analytics
# Designation : Data Analyst
# ---------------------------------------------------------

st.header("Employee Information")
st.write("**Employee :** Rahul Sharma")
st.write("**Department :** Analytics")
st.write("**Designation :** Data Analyst")

# ---------------------------------------------------------
# Gross Salary     Net Salary     Deductions     Paid Days
# ₹105,000         ₹95,000         ₹10,000          31
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Gross Salary", "₹105,000")
col2.metric("Net Salary", "₹95,000")
col3.metric("Deductions", "₹10,000")
col4.metric("Paid Days", "31")

st.divider()

# ---------------------------------------------------------
# Salary Components (Bar Chart)
# ---------------------------------------------------------

salary = pd.DataFrame({
    "Component": ["Basic Salary", "HRA", "Medical", "Special Allowance", "Bonus"],
    "Amount": [60000, 24000, 4000, 9000, 5000]
})

st.subheader("Salary Components (Bar Chart)")

fig, ax = plt.subplots()
ax.bar(salary["Component"], salary["Amount"])
plt.xticks(rotation=20)
st.pyplot(fig)

# ---------------------------------------------------------
# Earnings Distribution (Pie Chart)
# ---------------------------------------------------------

st.subheader("Earnings Distribution (Pie Chart)")

fig, ax = plt.subplots()
ax.pie(
    salary["Amount"],
    labels=salary["Component"],
    autopct="%1.1f%%",
    startangle=90
)
ax.axis("equal")
st.pyplot(fig)

# ---------------------------------------------------------
# Gross vs Deduction vs Net (Bar Chart)
# ---------------------------------------------------------

st.subheader("Gross vs Deduction vs Net (Bar Chart)")

fig, ax = plt.subplots()
ax.bar(
    ["Gross", "Deduction", "Net"],
    [105000, 10000, 95000]
)
st.pyplot(fig)

# ---------------------------------------------------------
# Employee Details
# Bank Name
# Account Number
# PAN
# Joining Date
# ---------------------------------------------------------

st.subheader("Employee Details")

details = pd.DataFrame({
    "Field": [
        "Bank Name",
        "Account Number",
        "PAN",
        "Joining Date"
    ],
    "Value": [
        "State Bank of India",
        "123456789012",
        "ABCDE1234F",
        "15-Jan-2023"
    ]
})

st.table(details)
