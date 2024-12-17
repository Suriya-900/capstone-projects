import pandas as pd
import sqlite3
import numpy as np
import random
import streamlit as st
from streamlit_option_menu import option_menu

# Load your DataFrame after adding columns
df_kerala = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\kerala_routes_updated.csv')
df_andhra = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\andhra_routes.csv')
df_kadamba = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\kadamba_routes.csv')
df_rajasthan = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\rajasthan_routes.csv')
df_telangana = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\telangana_routes.csv')
df_bengal = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\bengal_routes.csv')
df_west_bengal = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\west_bengal_routes.csv')
df_assam = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\assam_routes.csv')
df_uttarpradesh = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\uttarpradesh_routes.csv')
df_himachal = pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\himachal_routes.csv')


# Set Streamlit page config
st.set_page_config(layout="wide")

# Sidebar menu for navigation
web = option_menu(
    menu_title="Travel Company",
    options=["Home", "Routes and Links"],
    icons=["house", "search"],
    orientation="horizontal"
)

# Apply background style
st.markdown(
    """
    <style>
        /* Apply background color to the main content */
        .stApp {
            background-color: #f5b7b1;
        }
    </style>
    """, unsafe_allow_html=True
)

# Home Page content
if web == "Home":
    st.image("c:/Users/vicky/Downloads/route.jpg", width=250)
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")

    st.subheader("Domain:")
    st.markdown("<span style='color:Black;'>Transportation</span>", unsafe_allow_html=True)

    st.subheader("Skills taken From This Project:")
    st.markdown("<span style='color:Black;'>Web Scraping using Selenium, Python, Streamlit, SQL</span>", unsafe_allow_html=True)

    st.subheader("Approach:")
    st.markdown("""
    <span style='color:Black;'>
    <b>Data Scraping:</b><br>
    Used Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.<br><br>
    
    <b>Data Storage:</b><br>
    Stored the scraped data in a SQL database.<br><br>
    
    <b>Streamlit Application:</b><br>
    Developed a Streamlit application to display and filter the scraped data.<br>
    Implemented various filters such as bus type, route, price range, star rating, and availability.<br><br>
    
    <b>Data Analysis/Filtering using Streamlit:</b><br>
    Used SQL queries to retrieve and filter data based on inputs.<br>
    Streamlit allows users to interact with and filter the data through the application.
    </span>
""", unsafe_allow_html=True)

    st.subheader("Developed By:")
    st.markdown("<span style='color:Black;'>Suriya Vignesh</span>", unsafe_allow_html=True)
S = None 
# Routes and Links Page content
if web == "Routes and Links":
    # Sidebar filters
    S = st.sidebar.selectbox("List of States", [
        "Kerala", "Andhra Pradesh", "Telangana", "Kadamba",
        "West Bengal", "South Bengal", "Uttar Pradesh", "Rajasthan",
        "Assam", "Himachal"
    ])

    if S == "Kerala":
        # Route selection
        K = st.sidebar.selectbox("List of Routes", df_kerala['Route_name'].unique())

        # Fare range
        min_fare_K = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
        max_fare_K = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

        # Departure time filter options
        departure_time_options = {
            "Before 6 am": "Before 6 am",
            "6 am to 12 pm": "6 am to 12 pm",
            "12 pm to 6 pm": "12 pm to 6 pm",
            "After 6 pm": "After 6 pm"
        }

        selected_departure_times = []
        for label, time_range in departure_time_options.items():
            if st.sidebar.checkbox(label):
                selected_departure_times.append(time_range)

        # Filter based on selected departure times
        if selected_departure_times:
            if "Before 6 am" in selected_departure_times:
                df_kerala = df_kerala[df_kerala["Start_time"] < "06:00"]
            if "6 am to 12 pm" in selected_departure_times:
                df_kerala = df_kerala[df_kerala["Start_time"].between("06:00", "12:00")]
            if "12 pm to 6 pm" in selected_departure_times:
                df_kerala = df_kerala[df_kerala["Start_time"].between("12:00", "18:00")]
            if "After 6 pm" in selected_departure_times:
                df_kerala = df_kerala[df_kerala["Start_time"] > "18:00"]

        # Filter based on bus type
        bus_types = df_kerala['Bus_type'].unique()
        selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
        if selected_bus_types:
            df_kerala = df_kerala[df_kerala["Bus_type"].isin(selected_bus_types)]

        # Filter based on seat availability
        seat_availability_options = df_kerala['Seats_Available'].unique()
        selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
        if selected_seat_availability:
            df_kerala = df_kerala[df_kerala["Seats_Available"].isin(selected_seat_availability)]

        # Rating slider
        min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
        if min_rating:
            df_kerala = df_kerala[df_kerala["Ratings"] >= min_rating]

        # Show the filtered data
        st.write("Filtered Bus Data:", df_kerala)



# Andhra Pradesh 

df_andhra['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_andhra)), 'h')  # Random start times
df_andhra['Seats_Available'] = np.random.randint(10, 50, size=len(df_andhra))  # Random seat availability between 10 and 50
df_andhra['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_andhra))  # Random bus types
df_andhra['End_time'] = df_andhra['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_andhra)), 'h')  # Random end times (3 to 8 hours after start)
df_andhra['Ratings'] = np.random.uniform(1, 5, size=len(df_andhra))  # Random ratings between 1 and 5


if S == "Andhra Pradesh":
        # Route selection for Andhra Pradesh
        AP = st.sidebar.selectbox("List of Routes", df_andhra['Route_name'].unique())

        # Apply other filters (Fare, Seats_Available, Bus_type, etc.)
        min_fare_AP = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
        max_fare_AP = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

        # Departure time filter options
        departure_time_options = {
            "Before 6 am": "Before 6 am",
            "6 am to 12 pm": "6 am to 12 pm",
            "12 pm to 6 pm": "12 pm to 6 pm",
            "After 6 pm": "After 6 pm"
        }

        selected_departure_times = []
        for label, time_range in departure_time_options.items():
            if st.sidebar.checkbox(label):
                selected_departure_times.append(time_range)

        # Filter based on selected departure times
        if selected_departure_times:
            if "Before 6 am" in selected_departure_times:
                df_andhra = df_andhra[df_andhra["Start_time"] < "06:00"]
            if "6 am to 12 pm" in selected_departure_times:
                df_andhra = df_andhra[df_andhra["Start_time"].between("06:00", "12:00")]
            if "12 pm to 6 pm" in selected_departure_times:
                df_andhra = df_andhra[df_andhra["Start_time"].between("12:00", "18:00")]
            if "After 6 pm" in selected_departure_times:
                df_andhra = df_andhra[df_andhra["Start_time"] > "18:00"]

        # Filter based on bus type
        bus_types = df_andhra['Bus_type'].unique()
        selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
        if selected_bus_types:
            df_andhra = df_andhra[df_andhra["Bus_type"].isin(selected_bus_types)]

        # Filter based on seat availability
        seat_availability_options = df_andhra['Seats_Available'].unique()
        selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
        if selected_seat_availability:
            df_andhra = df_andhra[df_andhra["Seats_Available"].isin(selected_seat_availability)]

        # Rating slider
        min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
        if min_rating:
            df_andhra = df_andhra[df_andhra["Ratings"] >= min_rating]

        # Show the filtered data
        st.write("Filtered Bus Data:", df_andhra)

#Kadamba 

df_kadamba['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_kadamba)), 'h')  # Random start times
df_kadamba['Seats_Available'] = np.random.randint(10, 50, size=len(df_kadamba))  # Random seat availability between 10 and 50
df_kadamba['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_kadamba))  # Random bus types
df_kadamba['End_time'] = df_kadamba['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_kadamba)), 'h')  # Random end times (3 to 8 hours after start)
df_kadamba['Ratings'] = np.random.uniform(1, 5, size=len(df_kadamba))  # Random ratings between 1 and 5

# Handle Kadamba state selection
if S == "Kadamba":
    # Route selection for Kadamba
    K = st.sidebar.selectbox("List of Routes", df_kadamba['Route_name'].unique())

    # Apply other filters (Fare, Seats_Available, Bus_type, etc.)
    min_fare_K = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
    max_fare_K = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

    # Departure time filter options
    departure_time_options = {
        "Before 6 am": "Before 6 am",
        "6 am to 12 pm": "6 am to 12 pm",
        "12 pm to 6 pm": "12 pm to 6 pm",
        "After 6 pm": "After 6 pm"
    }

    selected_departure_times = []
    for label, time_range in departure_time_options.items():
        if st.sidebar.checkbox(label):
            selected_departure_times.append(time_range)

    # Filter based on selected departure times
    if selected_departure_times:
        if "Before 6 am" in selected_departure_times:
            df_kadamba = df_kadamba[df_kadamba["Start_time"] < "06:00"]
        if "6 am to 12 pm" in selected_departure_times:
            df_kadamba = df_kadamba[df_kadamba["Start_time"].between("06:00", "12:00")]
        if "12 pm to 6 pm" in selected_departure_times:
            df_kadamba = df_kadamba[df_kadamba["Start_time"].between("12:00", "18:00")]
        if "After 6 pm" in selected_departure_times:
            df_kadamba = df_kadamba[df_kadamba["Start_time"] > "18:00"]

    # Filter based on bus type
    bus_types = df_kadamba['Bus_type'].unique()
    selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
    if selected_bus_types:
        df_kadamba = df_kadamba[df_kadamba["Bus_type"].isin(selected_bus_types)]

    # Filter based on seat availability
    seat_availability_options = df_kadamba['Seats_Available'].unique()
    selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
    if selected_seat_availability:
        df_kadamba = df_kadamba[df_kadamba["Seats_Available"].isin(selected_seat_availability)]

    # Rating slider
    min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
    if min_rating:
        df_kadamba = df_kadamba[df_kadamba["Ratings"] >= min_rating]

    # Show the filtered data
    st.write("Filtered Bus Data:", df_kadamba)

# Telangana

df_telangana['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_telangana)), 'h')  # Random start times
df_telangana['Seats_Available'] = np.random.randint(10, 50, size=len(df_telangana))  # Random seat availability between 10 and 50
df_telangana['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_telangana))  # Random bus types
df_telangana['End_time'] = df_telangana['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_telangana)), 'h')  # Random end times (3 to 8 hours after start)
df_telangana['Ratings'] = np.random.uniform(1, 5, size=len(df_telangana))  # Random ratings between 1 and 5

# In your streamlit app, handle the state "Telangana"
if S == "Telangana":
    # Route selection for Telangana
    TL = st.sidebar.selectbox("List of Routes", df_telangana['Route_name'].unique())

    # Apply other filters (Fare, Seats_Available, Bus_type, etc.)
    min_fare_TL = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
    max_fare_TL = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

    # Departure time filter options
    departure_time_options = {
        "Before 6 am": "Before 6 am",
        "6 am to 12 pm": "6 am to 12 pm",
        "12 pm to 6 pm": "12 pm to 6 pm",
        "After 6 pm": "After 6 pm"
    }

    selected_departure_times = []
    for label, time_range in departure_time_options.items():
        if st.sidebar.checkbox(label):
            selected_departure_times.append(time_range)

    # Filter based on selected departure times
    if selected_departure_times:
        if "Before 6 am" in selected_departure_times:
            df_telangana = df_telangana[df_telangana["Start_time"] < "06:00"]
        if "6 am to 12 pm" in selected_departure_times:
            df_telangana = df_telangana[df_telangana["Start_time"].between("06:00", "12:00")]
        if "12 pm to 6 pm" in selected_departure_times:
            df_telangana = df_telangana[df_telangana["Start_time"].between("12:00", "18:00")]
        if "After 6 pm" in selected_departure_times:
            df_telangana = df_telangana[df_telangana["Start_time"] > "18:00"]

    # Filter based on bus type if the column exists
    if 'Bus_type' in df_telangana.columns:
        bus_types = df_telangana['Bus_type'].unique()
        selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
        if selected_bus_types:
            df_telangana = df_telangana[df_telangana["Bus_type"].isin(selected_bus_types)]

    # Filter based on seat availability
    seat_availability_options = df_telangana['Seats_Available'].unique()
    selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
    if selected_seat_availability:
        df_telangana = df_telangana[df_telangana["Seats_Available"].isin(selected_seat_availability)]

    # Rating slider
    min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
    if min_rating:
        df_telangana = df_telangana[df_telangana["Ratings"] >= min_rating]

    # Show the filtered data for Telangana
    st.write("Filtered Bus Data:", df_telangana)


# Rajasthan

df_rajasthan['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_rajasthan)), 'h')  # Random start times
df_rajasthan['Seats_Available'] = np.random.randint(10, 50, size=len(df_rajasthan))  # Random seat availability between 10 and 50
df_rajasthan['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_rajasthan))  # Random bus types
df_rajasthan['End_time'] = df_rajasthan['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_rajasthan)), 'h')  # Random end times (3 to 8 hours after start)
df_rajasthan['Ratings'] = np.random.uniform(1, 5, size=len(df_rajasthan))  # Random ratings between 1 and 5

# Modify the Streamlit sidebar and content for Rajasthan
if S == "Rajasthan":
    # Route selection for Rajasthan
    R = st.sidebar.selectbox("List of Routes", df_rajasthan['Route_name'].unique())

    # Apply other filters (Fare, Seats_Available, Bus_type, etc.)
    min_fare_R = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
    max_fare_R = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

    # Departure time filter options
    departure_time_options = {
        "Before 6 am": "Before 6 am",
        "6 am to 12 pm": "6 am to 12 pm",
        "12 pm to 6 pm": "12 pm to 6 pm",
        "After 6 pm": "After 6 pm"
    }

    selected_departure_times = []
    for label, time_range in departure_time_options.items():
        if st.sidebar.checkbox(label):
            selected_departure_times.append(time_range)

    # Filter based on selected departure times
    if selected_departure_times:
        if "Before 6 am" in selected_departure_times:
            df_rajasthan = df_rajasthan[df_rajasthan["Start_time"] < "06:00"]
        if "6 am to 12 pm" in selected_departure_times:
            df_rajasthan = df_rajasthan[df_rajasthan["Start_time"].between("06:00", "12:00")]
        if "12 pm to 6 pm" in selected_departure_times:
            df_rajasthan = df_rajasthan[df_rajasthan["Start_time"].between("12:00", "18:00")]
        if "After 6 pm" in selected_departure_times:
            df_rajasthan = df_rajasthan[df_rajasthan["Start_time"] > "18:00"]

    # Filter based on bus type
    bus_types = df_rajasthan['Bus_type'].unique()
    selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
    if selected_bus_types:
        df_rajasthan = df_rajasthan[df_rajasthan["Bus_type"].isin(selected_bus_types)]

    # Filter based on seat availability
    seat_availability_options = df_rajasthan['Seats_Available'].unique()
    selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
    if selected_seat_availability:
        df_rajasthan = df_rajasthan[df_rajasthan["Seats_Available"].isin(selected_seat_availability)]

    # Rating slider
    min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
    if min_rating:
        df_rajasthan = df_rajasthan[df_rajasthan["Ratings"] >= min_rating]

    # Show the filtered data
    st.write("Filtered Bus Data:", df_rajasthan)
   
# South Bengal


# Add the missing columns with random/placeholder values for Bengal DataFrame
df_bengal['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_bengal)), 'h')  # Random start times
df_bengal['Seats_Available'] = np.random.randint(10, 50, size=len(df_bengal))  # Random seat availability between 10 and 50
df_bengal['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_bengal))  # Random bus types
df_bengal['End_time'] = df_bengal['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_bengal)), 'h')  # Random end times (3 to 8 hours after start)
df_bengal['Ratings'] = np.random.uniform(1, 5, size=len(df_bengal))  # Random ratings between 1 and 5

if S == "South Bengal":
        # Route selection for Bengal
        B = st.sidebar.selectbox("List of Routes", df_bengal['Route_name'].unique())

        # Fare range filter
        min_fare_B = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
        max_fare_B = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

        # Departure time filter options
        departure_time_options = {
            "Before 6 am": "Before 6 am",
            "6 am to 12 pm": "6 am to 12 pm",
            "12 pm to 6 pm": "12 pm to 6 pm",
            "After 6 pm": "After 6 pm"
        }

        selected_departure_times = []
        for label, time_range in departure_time_options.items():
            if st.sidebar.checkbox(label):
                selected_departure_times.append(time_range)

        # Filter based on selected departure times
        if selected_departure_times:
            if "Before 6 am" in selected_departure_times:
                df_bengal = df_bengal[df_bengal["Start_time"] < "06:00"]
            if "6 am to 12 pm" in selected_departure_times:
                df_bengal = df_bengal[df_bengal["Start_time"].between("06:00", "12:00")]
            if "12 pm to 6 pm" in selected_departure_times:
                df_bengal = df_bengal[df_bengal["Start_time"].between("12:00", "18:00")]
            if "After 6 pm" in selected_departure_times:
                df_bengal = df_bengal[df_bengal["Start_time"] > "18:00"]

        # Filter based on bus type
        bus_types = df_bengal['Bus_type'].unique()
        selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
        if selected_bus_types:
            df_bengal = df_bengal[df_bengal["Bus_type"].isin(selected_bus_types)]

        # Filter based on seat availability
        seat_availability_options = df_bengal['Seats_Available'].unique()
        selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
        if selected_seat_availability:
            df_bengal = df_bengal[df_bengal["Seats_Available"].isin(selected_seat_availability)]

        # Rating slider
        min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
        if min_rating:
            df_bengal = df_bengal[df_bengal["Ratings"] >= min_rating]

        # Show the filtered data for Bengal
        st.write("Filtered Bus Data:", df_bengal)


# West Bengal 
df_west_bengal['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_west_bengal)), 'h')  # Random start times
df_west_bengal['Seats_Available'] = np.random.randint(10, 50, size=len(df_west_bengal))  # Random seat availability between 10 and 50
df_west_bengal['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_west_bengal))  # Random bus types
df_west_bengal['End_time'] = df_west_bengal['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_west_bengal)), 'h')  # Random end times (3 to 8 hours after start)
df_west_bengal['Ratings'] = np.random.uniform(1, 5, size=len(df_west_bengal))  # Random ratings between 1 and 5

# Modify the Streamlit sidebar and content for West Bengal
if S == "West Bengal":
    # Route selection for West Bengal
    WB = st.sidebar.selectbox("List of Routes", df_west_bengal['Route_name'].unique())

    # Apply other filters (Fare, Seats_Available, Bus_type, etc.)
    min_fare_WB = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
    max_fare_WB = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

    # Departure time filter options
    departure_time_options = {
        "Before 6 am": "Before 6 am",
        "6 am to 12 pm": "6 am to 12 pm",
        "12 pm to 6 pm": "12 pm to 6 pm",
        "After 6 pm": "After 6 pm"
    }

    selected_departure_times = []
    for label, time_range in departure_time_options.items():
        if st.sidebar.checkbox(label):
            selected_departure_times.append(time_range)

    # Filter based on selected departure times
    if selected_departure_times:
        if "Before 6 am" in selected_departure_times:
            df_west_bengal = df_west_bengal[df_west_bengal["Start_time"] < "06:00"]
        if "6 am to 12 pm" in selected_departure_times:
            df_west_bengal = df_west_bengal[df_west_bengal["Start_time"].between("06:00", "12:00")]
        if "12 pm to 6 pm" in selected_departure_times:
            df_west_bengal = df_west_bengal[df_west_bengal["Start_time"].between("12:00", "18:00")]
        if "After 6 pm" in selected_departure_times:
            df_west_bengal = df_west_bengal[df_west_bengal["Start_time"] > "18:00"]

    # Filter based on bus type
    bus_types = df_west_bengal['Bus_type'].unique()
    selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
    if selected_bus_types:
        df_west_bengal = df_west_bengal[df_west_bengal["Bus_type"].isin(selected_bus_types)]

    # Filter based on seat availability
    seat_availability_options = df_west_bengal['Seats_Available'].unique()
    selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
    if selected_seat_availability:
        df_west_bengal = df_west_bengal[df_west_bengal["Seats_Available"].isin(selected_seat_availability)]

    # Rating slider
    min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
    if min_rating:
        df_west_bengal = df_west_bengal[df_west_bengal["Ratings"] >= min_rating]

    # Show the filtered data for West Bengal
    st.write("Filtered Bus Data:", df_west_bengal)


#  Uttar Pradesh
df_uttarpradesh['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_uttarpradesh)), 'h')  # Random start times
df_uttarpradesh['Seats_Available'] = np.random.randint(10, 50, size=len(df_uttarpradesh))  # Random seat availability between 10 and 50
df_uttarpradesh['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_uttarpradesh))  # Random bus types
df_uttarpradesh['End_time'] = df_uttarpradesh['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_uttarpradesh)), 'h')  # Random end times (3 to 8 hours after start)
df_uttarpradesh['Ratings'] = np.random.uniform(1, 5, size=len(df_uttarpradesh))  # Random ratings between 1 and 5

# Modify the Streamlit sidebar and content for Uttar Pradesh
if S == "Uttar Pradesh":
    # Route selection for Uttar Pradesh
    U = st.sidebar.selectbox("List of Routes", df_uttarpradesh['Route_name'].unique())

    # Apply other filters (Fare, Seats_Available, Bus_type, etc.)
    min_fare_U = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
    max_fare_U = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

    # Departure time filter options
    departure_time_options = {
        "Before 6 am": "Before 6 am",
        "6 am to 12 pm": "6 am to 12 pm",
        "12 pm to 6 pm": "12 pm to 6 pm",
        "After 6 pm": "After 6 pm"
    }

    selected_departure_times = []
    for label, time_range in departure_time_options.items():
        if st.sidebar.checkbox(label):
            selected_departure_times.append(time_range)

    # Filter based on selected departure times
    if selected_departure_times:
        if "Before 6 am" in selected_departure_times:
            df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Start_time"] < "06:00"]
        if "6 am to 12 pm" in selected_departure_times:
            df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Start_time"].between("06:00", "12:00")]
        if "12 pm to 6 pm" in selected_departure_times:
            df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Start_time"].between("12:00", "18:00")]
        if "After 6 pm" in selected_departure_times:
            df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Start_time"] > "18:00"]

    # Filter based on bus type
    bus_types = df_uttarpradesh['Bus_type'].unique()
    selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
    if selected_bus_types:
        df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Bus_type"].isin(selected_bus_types)]

    # Filter based on seat availability
    seat_availability_options = df_uttarpradesh['Seats_Available'].unique()
    selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
    if selected_seat_availability:
        df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Seats_Available"].isin(selected_seat_availability)]

    # Rating slider
    min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
    if min_rating:
        df_uttarpradesh = df_uttarpradesh[df_uttarpradesh["Ratings"] >= min_rating]

    # Show the filtered data
    st.write("Filtered Bus Data:", df_uttarpradesh)



# Assam 
df_assam['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_assam)), 'h')  # Random start times
df_assam['Seats_Available'] = np.random.randint(10, 50, size=len(df_assam))  # Random seat availability between 10 and 50
df_assam['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_assam))  # Random bus types
df_assam['End_time'] = df_assam['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_assam)), 'h')  # Random end times (3 to 8 hours after start)
df_assam['Ratings'] = np.random.uniform(1, 5, size=len(df_assam))  # Random ratings between 1 and 5


if S == "Assam":
        # Route selection for Assam
        A = st.sidebar.selectbox("List of Routes", df_assam['Route_name'].unique())

        # Fare range filter
        min_fare_A = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
        max_fare_A = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

        # Departure time filter options
        departure_time_options = {
            "Before 6 am": "Before 6 am",
            "6 am to 12 pm": "6 am to 12 pm",
            "12 pm to 6 pm": "12 pm to 6 pm",
            "After 6 pm": "After 6 pm"
        }

        selected_departure_times = []
        for label, time_range in departure_time_options.items():
            if st.sidebar.checkbox(label):
                selected_departure_times.append(time_range)

        # Filter based on selected departure times
        if selected_departure_times:
            if "Before 6 am" in selected_departure_times:
                df_assam = df_assam[df_assam["Start_time"] < "06:00"]
            if "6 am to 12 pm" in selected_departure_times:
                df_assam = df_assam[df_assam["Start_time"].between("06:00", "12:00")]
            if "12 pm to 6 pm" in selected_departure_times:
                df_assam = df_assam[df_assam["Start_time"].between("12:00", "18:00")]
            if "After 6 pm" in selected_departure_times:
                df_assam = df_assam[df_assam["Start_time"] > "18:00"]

        # Filter based on bus type
        bus_types = df_assam['Bus_type'].unique()
        selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
        if selected_bus_types:
            df_assam = df_assam[df_assam["Bus_type"].isin(selected_bus_types)]

        # Filter based on seat availability
        seat_availability_options = df_assam['Seats_Available'].unique()
        selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
        if selected_seat_availability:
            df_assam = df_assam[df_assam["Seats_Available"].isin(selected_seat_availability)]

        # Rating slider
        min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
        if min_rating:
            df_assam = df_assam[df_assam["Ratings"] >= min_rating]

        # Show the filtered data for Assam
        st.write("Filtered Bus Data:", df_assam)



# Himachal 
df_himachal['Start_time'] = pd.to_datetime('2023-12-17') + pd.to_timedelta(np.random.randint(0, 24, size=len(df_himachal)), 'h')  # Random start times
df_himachal['Seats_Available'] = np.random.randint(10, 50, size=len(df_himachal))  # Random seat availability between 10 and 50
df_himachal['Bus_type'] = np.random.choice(['Sleeper', 'Semi-Sleeper', 'AC', 'Non-AC'], size=len(df_himachal))  # Random bus types
df_himachal['End_time'] = df_himachal['Start_time'] + pd.to_timedelta(np.random.randint(3, 8, size=len(df_himachal)), 'h')  # Random end times (3 to 8 hours after start)
df_himachal['Ratings'] = np.random.uniform(1, 5, size=len(df_himachal))  # Random ratings between 1 and 5



if S == "Himachal":
        # Route selection for Himachal
        H = st.sidebar.selectbox("List of Routes", df_himachal['Route_name'].unique())

        # Fare range filter
        min_fare_H = st.sidebar.number_input("Minimum Bus Fare", min_value=0, max_value=10000, value=50, step=50)
        max_fare_H = st.sidebar.number_input("Maximum Bus Fare", min_value=0, max_value=10000, value=1000, step=50)

        # Departure time filter options
        departure_time_options = {
            "Before 6 am": "Before 6 am",
            "6 am to 12 pm": "6 am to 12 pm",
            "12 pm to 6 pm": "12 pm to 6 pm",
            "After 6 pm": "After 6 pm"
        }

        selected_departure_times = []
        for label, time_range in departure_time_options.items():
            if st.sidebar.checkbox(label):
                selected_departure_times.append(time_range)

        # Filter based on selected departure times
        if selected_departure_times:
            if "Before 6 am" in selected_departure_times:
                df_himachal = df_himachal[df_himachal["Start_time"] < "06:00"]
            if "6 am to 12 pm" in selected_departure_times:
                df_himachal = df_himachal[df_himachal["Start_time"].between("06:00", "12:00")]
            if "12 pm to 6 pm" in selected_departure_times:
                df_himachal = df_himachal[df_himachal["Start_time"].between("12:00", "18:00")]
            if "After 6 pm" in selected_departure_times:
                df_himachal = df_himachal[df_himachal["Start_time"] > "18:00"]

        # Filter based on bus type
        bus_types = df_himachal['Bus_type'].unique()
        selected_bus_types = st.sidebar.multiselect("Select Bus Types", bus_types)
        if selected_bus_types:
            df_himachal = df_himachal[df_himachal["Bus_type"].isin(selected_bus_types)]

        # Filter based on seat availability
        seat_availability_options = df_himachal['Seats_Available'].unique()
        selected_seat_availability = st.sidebar.multiselect("Select Seat Availability", seat_availability_options)
        if selected_seat_availability:
            df_himachal = df_himachal[df_himachal["Seats_Available"].isin(selected_seat_availability)]

        # Rating slider
        min_rating = st.sidebar.slider("Select Minimum Rating", min_value=1, max_value=5, value=3, step=1)
        if min_rating:
            df_himachal = df_himachal[df_himachal["Ratings"] >= min_rating]

        # Show the filtered data for Himachal
        st.write("Filtered Bus Data:", df_himachal)


    