import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set up the Streamlit app title and layout with Duke branding
st.set_page_config(
    page_title="Duke Divinity School Enrollment Insights",
    page_icon="📘",
    layout="wide",
)

# Duke color palette
DUKE_BLUE = "#012169"
LIGHT_BLUE = "#6CACE4"
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

admissions_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024],
    "Applications": [300, 350, 400, 450],
    "Enrollments": [120, 130, 150, 160],
    "Acceptance Rate (%)": [40.0, 37.1, 37.5, 35.6],
})

# Sidebar navigation with logo
st.sidebar.image("https://divinity.duke.edu/sites/divinity.duke.edu/files/duke_divinity_logo.png", use_column_width=True)
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Academic Programs", "Faculty Directory", "Admissions Dashboard", "Event Calendar"])

# Home Page
if menu == "Home":
    st.title("Welcome to Duke Divinity School Insights 📘")
    st.image("https://divinity.duke.edu/sites/divinity.duke.edu/files/styles/hero_full/public/2021-03/div_homepage.jpg", use_column_width=True)
    st.write(
        """
        This web application provides insights into academic programs, admissions trends, faculty information,
        and events at Duke Divinity School. Use the navigation menu to explore the different sections.
        """
    )

    st.metric(label="Programs Offered", value="4")
    st.metric(label="Faculty Members", value="25")
    st.metric(label="Upcoming Events", value="3")

# Academic Programs
elif menu == "Academic Programs":
    st.title("Academic Programs Overview")
    st.write("Explore the degree programs offered at Duke Divinity School:")
    st.table(programs_data)

    st.subheader("Program Cost Analysis")
    fig = px.bar(
        programs_data,
        x="Program Name",
        y="Tuition (USD)",
        color="Program Name",
        color_discrete_sequence=[DUKE_BLUE, LIGHT_BLUE, GRAY, WHITE],
        title="Tuition Costs by Program",
    )
    st.plotly_chart(fig, use_container_width=True)

# Faculty Directory
elif menu == "Faculty Directory":
    st.title("Faculty Directory")
    st.write("Meet our distinguished faculty members:")
    st.table(faculty_data)

# Admissions Dashboard
elif menu == "Admissions Dashboard":
    st.title("Admissions Dashboard")
    st.write("This dashboard provides insights into admissions data:")

    # Key Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Applications (2024)", "450", delta="50 from 2023")
    col2.metric("Enrollments (2024)", "160", delta="10 from 2023")
    col3.metric("Acceptance Rate", "35.6%", delta="-1.9%")

    # Admissions Trends
    st.subheader("Admissions Trends Over Time")
    fig = px.line(
        admissions_data,
        x="Year",
        y=["Applications", "Enrollments"],
        markers=True,
        title="Applications and Enrollments Over Time",
        color_discrete_sequence=[DUKE_BLUE, LIGHT_BLUE],
    )
    st.plotly_chart(fig, use_container_width=True)

# Event Calendar
elif menu == "Event Calendar":
    st.title("Event Calendar")
    st.write("Discover upcoming events at Duke Divinity School:")
    st.table(event_data)

    st.subheader("Event Locations")
    fig = px.histogram(
        event_data,
        x="Location",
        title="Event Count by Location",
        color_discrete_sequence=[DUKE_BLUE],
    )
    st.plotly_chart(fig, use_container_width=True)

st.sidebar.write("Developed for Duke Divinity School (Mock Data Prototype).")

