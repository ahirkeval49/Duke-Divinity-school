import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Streamlit app title and layout with Duke branding
st.set_page_config(
    page_title="Duke Divinity School Enrollment Insights",
    page_icon="📘",
    layout="wide",
)

# Apply Duke color palette for charts
DUKE_BLUE = "#012169"
WHITE = "#FFFFFF"
GRAY = "#A6A6A6"

# Mock data
programs_data = pd.DataFrame({
    "Program Name": ["Master of Divinity", "Master of Theology", "Doctor of Ministry", "Certificate in Theology"],
    "Duration (Years)": [3, 1, 3, 1],
    "Credit Hours": [90, 30, 36, 12],
    "Tuition (USD)": [45000, 15000, 20000, 6000],
})

faculty_data = pd.DataFrame({
    "Name": ["Dr. Alice Smith", "Dr. Bob Johnson", "Dr. Clara Wright", "Dr. David Lee"],
    "Department": ["Theology", "Biblical Studies", "Church History", "Pastoral Studies"],
    "Email": ["alice.smith@duke.edu", "bob.johnson@duke.edu", "clara.wright@duke.edu", "david.lee@duke.edu"],
})

event_data = pd.DataFrame({
    "Event Name": ["Open House", "Lecture: Faith & Science", "Seminary Life Workshop"],
    "Date": ["2025-02-15", "2025-03-10", "2025-04-05"],
    "Location": ["Virtual", "Campus - Room 101", "Campus - Chapel Hall"],
    "Description": ["Meet the faculty and explore programs.",
                    "A discussion on the intersection of faith and science.",
                    "Workshop on navigating seminary life."],
})

# Navigation sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Academic Programs", "Faculty Directory", "Admissions Dashboard", "Event Calendar"])

# Add Duke Divinity School Logo
st.sidebar.image("https://divinity.duke.edu/sites/divinity.duke.edu/files/styles/hero_full/public/2021-03/div_homepage.jpg",https://divinity.duke.edu/themes/custom/divinity_2023/logo.svg, use_column_width=True)

# Home Page
if menu == "Home":
    st.title("Welcome to Duke Divinity School Insights 📘")
    st.image("https://divinity.duke.edu/sites/divinity.duke.edu/files/duke_divinity_logo.png",https://divinity.duke.edu/themes/custom/divinity_2023/logo.svg, use_column_width=True)
    st.write(
        """
        This web application provides insights into academic programs, admissions trends, faculty information,
        and events at Duke Divinity School. Use the navigation menu to explore the different sections.
        """
    )

# Academic Programs
elif menu == "Academic Programs":
    st.title("Academic Programs Overview")
    st.write("Explore the degree programs offered at Duke Divinity School:")
    st.table(programs_data.style.set_properties(**{
        'background-color': DUKE_BLUE,
        'color': WHITE,
        'border-color': GRAY,
    }))

    st.subheader("Program Cost Analysis")
    fig, ax = plt.subplots()
    sns.barplot(data=programs_data, x="Program Name", y="Tuition (USD)", palette=[DUKE_BLUE, GRAY], ax=ax)
    ax.set_title("Tuition Costs by Program", fontsize=16, color=DUKE_BLUE)
    ax.set_ylabel("Tuition (USD)", fontsize=12, color=DUKE_BLUE)
    ax.set_xlabel("Program Name", fontsize=12, color=DUKE_BLUE)
    st.pyplot(fig)

# Faculty Directory
elif menu == "Faculty Directory":
    st.title("Faculty Directory")
    st.write("Meet our distinguished faculty members:")
    st.table(faculty_data.style.set_properties(**{
        'background-color': DUKE_BLUE,
        'color': WHITE,
        'border-color': GRAY,
    }))

# Admissions Dashboard
elif menu == "Admissions Dashboard":
    st.title("Admissions Dashboard")
    st.write("This dashboard provides insights into admissions data (mock data for demo purposes):")

    # Mock admissions data
    admissions_data = pd.DataFrame({
        "Year": [2021, 2022, 2023, 2024],
        "Applications": [300, 350, 400, 450],
        "Enrollments": [120, 130, 150, 160],
        "Acceptance Rate (%)": [40.0, 37.1, 37.5, 35.6],
    })

    # Show data table
    st.subheader("Admissions Statistics")
    st.table(admissions_data.style.set_properties(**{
        'background-color': DUKE_BLUE,
        'color': WHITE,
        'border-color': GRAY,
    }))

    # Plot trends
    st.subheader("Admissions Trends")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(data=admissions_data, x="Year", y="Applications", marker="o", label="Applications", color=DUKE_BLUE, ax=ax)
    sns.lineplot(data=admissions_data, x="Year", y="Enrollments", marker="o", label="Enrollments", color=GRAY, ax=ax)
    ax.set_title("Admissions and Enrollment Trends", fontsize=16, color=DUKE_BLUE)
    ax.set_ylabel("Number of Students", fontsize=12, color=DUKE_BLUE)
    ax.set_xlabel("Year", fontsize=12, color=DUKE_BLUE)
    ax.legend()
    st.pyplot(fig)

# Event Calendar
elif menu == "Event Calendar":
    st.title("Event Calendar")
    st.write("Discover upcoming events at Duke Divinity School:")
    st.table(event_data.style.set_properties(**{
        'background-color': DUKE_BLUE,
        'color': WHITE,
        'border-color': GRAY,
    }))

    st.subheader("Event Locations")
    fig, ax = plt.subplots()
    sns.countplot(data=event_data, x="Location", palette=[DUKE_BLUE, GRAY], ax=ax)
    ax.set_title("Number of Events by Location", fontsize=16, color=DUKE_BLUE)
    ax.set_xlabel("Location", fontsize=12, color=DUKE_BLUE)
    ax.set_ylabel("Count", fontsize=12, color=DUKE_BLUE)
    st.pyplot(fig)

st.sidebar.write("Developed for Duke Divinity School (Mock Data Prototype).")
