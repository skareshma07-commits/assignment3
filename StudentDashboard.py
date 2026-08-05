import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("🎓 Student Performance Dashboard")

# -------------------------------
# Student Information
# -------------------------------
st.header("Student Information")

st.write("**Student Name:** Rahul Sharma")
st.write("**Roll Number:** 23DS101")
st.write("**Class:** B.Tech CSE-DS Final Year")

# -------------------------------
# KPI Cards
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Marks", "540")
col2.metric("Percentage", "90%")
col3.metric("Attendance", "95%")
col4.metric("Rank", "2")

st.divider()

# -------------------------------
# Subject-wise Marks
# -------------------------------
marks = pd.DataFrame({
    "Subject": [
        "Python",
        "DBMS",
        "Java",
        "AI",
        "ML",
        "Cloud"
    ],
    "Marks": [
        95,
        88,
        92,
        90,
        85,
        90
    ]
})

st.subheader("Subject-wise Marks (Bar Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(marks["Subject"], marks["Marks"])

ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")
ax.set_ylim(0,100)

st.pyplot(fig)

st.divider()

# -------------------------------
# Marks Distribution
# -------------------------------
st.subheader("Marks Distribution (Pie Chart)")

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    marks["Marks"],
    labels=marks["Subject"],
    autopct="%1.1f%%",
    startangle=90
)

st.pyplot(fig)

st.divider()

# -------------------------------
# Attendance Trend
# -------------------------------
st.subheader("Attendance Trend (Line Chart)")

attendance = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Attendance": [
        90,
        92,
        94,
        95,
        96,
        95
    ]
})

fig, ax = plt.subplots(figsize=(7,4))

ax.plot(
    attendance["Month"],
    attendance["Attendance"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Attendance (%)")
ax.set_ylim(80,100)

st.pyplot(fig)

st.divider()

# -------------------------------
# Student Details
# -------------------------------
st.subheader("Student Details Table")

details = pd.DataFrame({
    "Field": [
        "Department",
        "Section",
        "Semester",
        "Academic Year",
        "College"
    ],
    "Value": [
        "CSE-Data Science",
        "A",
        "8th",
        "2025-26",
        "XYZ Engineering College"
    ]
})

st.table(details)
