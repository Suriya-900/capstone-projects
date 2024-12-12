import pandas as pd
import sqlite3
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time


#Kerala bus
lists_K=[]
df_kerala=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\kerala_routes.csv')
for i,r in df_kerala.iterrows():
    lists_K.append(r["Route_name"])

#Andhra bus
lists_AP=[]
df_andhra=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\andhra_routes.csv')
for i,r in  df_andhra.iterrows():
    lists_AP.append(r["Route_name"])


#Telangana bus

lists_T=[]
df_telangana=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\telangana_routes.csv')
for i,r in df_telangana.iterrows():
    lists_T.append(r["Route_name"])


#Kadamba bus

lists_KM=[]
df_Kadamba=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\kadamba_routes.csv')
for i,r in df_Kadamba.iterrows():
    lists_KM.append(r["Route_name"])


#Rajasthan bus
lists_R=[]
df_Rajasthan=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\rajasthan_routes.csv')
for i,r in df_Rajasthan.iterrows():
    lists_R.append(r["Route_name"])

#Bengal bus

lists_SB=[]
df_Bengal=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\bengal_routes.csv')
for i,r in df_Bengal.iterrows():
    lists_SB.append(r["Route_name"])


#Himachal bus

lists_H=[]
df_Himachal=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\himachal_routes.csv')
for i,r in df_Himachal.iterrows():
    lists_H.append(r["Route_name"])


#Assam bus

lists_A=[]
df_Assam=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\assam_routes.csv')
for i,r in df_Assam.iterrows():
    lists_A.append(r["Route_name"])


#Uttarpradesh bus
lists_UP=[]
df_Uttarpradesh=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\uttarpradesh_routes.csv')
for i,r in df_Uttarpradesh.iterrows():
    lists_UP.append(r["Route_name"])


#WestBengal bus

lists_WB=[]
df_WestBengal=pd.read_csv(r'D:\guvi\redbus project\busroutesandlinks\west_bengal_routes.csv')
for i,r in df_WestBengal.iterrows():
    lists_WB.append(r["Route_name"])

#setting up  streamlit page

st.set_page_config(layout="wide")

web = option_menu(
    menu_title="Travel Company",
    options=["Home", "Routes and Links"],
    icons=["house", "search"],
    orientation="vertical"
)

#home page setting

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
if web == "Home":
    st.image("c:/Users/vicky/Downloads/route.jpg",width=250)
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


#  Routes and links page
if web =="Routes and Links":
    S=st.selectbox("List of States",["Kerala","Andhra Pradesh","Telangana","Kadamba","WestBengal","South Bengal","Uttar Pradesh","Rajasthan","Assam","Himachal"])
    select_fare=st.radio("Bus Fare Range",["50-1000","1000-2000","2000 and Above"]) 

 #Kerala busfare filtering
    if S == "Kerala":
        K = st.selectbox("List of Routes", lists_K)


        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
        
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                   WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                   ORDER BY Price DESC"""
        
            cursor.execute(query, (K,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
        
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                   WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                   ORDER BY Price DESC"""
        
            cursor.execute(query, (K,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
        
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                   WHERE price > 2000 AND Route_name = ?
                   ORDER BY Price DESC"""
        
            cursor.execute(query, (K,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])

            st.write(df_out)

#Andhra Fare Filtering

    if S == "Andhra Pradesh":
        AP = st.selectbox("List of Routes", lists_AP)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
        
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                   WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                   ORDER BY Price DESC"""
        
            cursor.execute(query, (AP,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
        
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                       WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                   ORDER BY Price DESC"""
        
            cursor.execute(query, (AP,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
        
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (AP,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

#Telengana Fare Filtering

    if S == "Telangana":
        T = st.selectbox("List of Routes", lists_T)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (T,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (T,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (T,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)



      
#Kadamba Fare Filtering 
    if S == "Kadamba":
        KM = st.selectbox("List of Routes", lists_KM)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (KM,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (KM,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (KM,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

#RajasthanFare Filtering

    if S == "Rajasthan":
        R = st.selectbox("List of Routes", lists_R)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (R,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (R,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (R,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

#South Bengal Fare Filtering

    if S == "South Bengal":
        SB = st.selectbox("List of Routes", lists_SB)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (SB,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (SB,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (SB,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

#Himachal Fare Filtering

    if S == "Himachal":
        H = st.selectbox("List of Routes", lists_H)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (H,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (H,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (H,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

 #Assam Fare Filtering
    if S == "Assam":
        A = st.selectbox("List of Routes", lists_A)
        
        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (A,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (A,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (A,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)


#Uttar Pradesh Fare Filtering

    if S == "Uttar Pradesh":
        UP = st.selectbox("List of Routes", lists_UP)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (UP,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (UP,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (UP,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

#West Bengal Fare Filtering

    if S == "West Bengal":
        WB = st.selectbox("List of Routes", lists_WB)

        if select_fare == "50-1000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 50 AND 1000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (WB,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "1000-2000":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price BETWEEN 1000 AND 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (WB,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

        if select_fare == "2000 and Above":
            df = pd.read_csv(r"D:\guvi\redbus project\sqlconn\Final_df.csv")

            conn = sqlite3.connect(r"D:\guvi\redbus project\sqlconn\redbus.db")
            
            df.to_sql("Final_df", conn, if_exists="replace", index=False)

            cursor = conn.cursor()

            query = """SELECT * FROM Final_df
                    WHERE price > 2000 AND Route_name = ?
                    ORDER BY Price DESC"""
            
            cursor.execute(query, (WB,))
            out = cursor.fetchall()

            df_out = pd.DataFrame(out, columns=["Bus_name", "Bus_type", "Start_time", "End_time", 
                                                "Total_duration", "Price", "Seats_Available", "Ratings", 
                                                "Route_link", "Route_name"])

            st.write(df_out)

