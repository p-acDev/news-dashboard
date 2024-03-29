import streamlit as st
from datetime import datetime
st.set_page_config(layout="wide")

# Initialize connection.
conn = st.connection("supabase", type="sql")

# filter date
cols = st.columns(2)
date1 = cols[0].date_input("De", format="YYYY-MM-DD", value=datetime(2024, 3, 3))
date2 = cols[1].date_input("A", format="YYYY-MM-DD")

# Perform query.
df = conn.query(f"""
                SELECT author, title, url, "publishedAt" FROM news WHERE "publishedAt" BETWEEN '{date1}' AND '{date2}';
                """)

st.dataframe(df)