import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("📊 ABC Store Sales Dashboard")

# -------------------------------
# Store Information
# -------------------------------
st.header("Store Information")

st.write("**Store Name:** ABC Store")
st.write("**Location:** Hyderabad")
st.write("**Manager:** Rahul Sharma")

# -------------------------------
# KPI Cards
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", "$250,000")
col2.metric("Profit", "$75,000")
col3.metric("Orders", "1,250")
col4.metric("Customers", "980")

st.divider()

# -------------------------------
# Monthly Sales
# -------------------------------
monthly_sales = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Sales": [
        30000,
        35000,
        42000,
        38000,
        50000,
        55000
    ]
})

st.subheader("Monthly Sales (Line Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Sales ($)")

st.pyplot(fig)

st.divider()

# -------------------------------
# Product Sales
# -------------------------------
product_sales = pd.DataFrame({
    "Product": [
        "Laptop",
        "Mobile",
        "Headphones",
        "Keyboard",
        "Mouse",
        "Monitor"
    ],
    "Sales": [
        60000,
        50000,
        30000,
        20000,
        15000,
        25000
    ]
})

st.subheader("Product Sales (Bar Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(
    product_sales["Product"],
    product_sales["Sales"]
)

ax.set_xlabel("Products")
ax.set_ylabel("Sales ($)")

st.pyplot(fig)

st.divider()

# -------------------------------
# Category Sales
# -------------------------------
category_sales = pd.DataFrame({
    "Category": [
        "Electronics",
        "Accessories",
        "Home Appliances",
        "Furniture"
    ],
    "Sales": [
        120000,
        50000,
        45000,
        35000
    ]
})

st.subheader("Category Sales (Pie Chart)")

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    category_sales["Sales"],
    labels=category_sales["Category"],
    autopct="%1.1f%%",
    startangle=90
)

st.pyplot(fig)

st.divider()

# -------------------------------
# Top Selling Products Table
# -------------------------------
st.subheader("Top Selling Products")

top_products = pd.DataFrame({
    "Product": [
        "Laptop",
        "Mobile",
        "Headphones",
        "Monitor",
        "Keyboard"
    ],
    "Units Sold": [
        320,
        280,
        240,
        180,
        160
    ],
    "Revenue ($)": [
        60000,
        50000,
        30000,
        25000,
        20000
    ]
})

st.table(top_products)
