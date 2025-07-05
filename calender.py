import streamlit as st
import calendar
from datetime import datetime
import pandas as pd

# Set page config
st.set_page_config(page_title="Yearly Calendar", layout="wide")

# Custom colors for month names
month_colors = [
    "#FF5733", "#33C1FF", "#FF33A6", "#75FF33",
    "#FFC300", "#DAF7A6", "#C70039", "#900C3F",
    "#581845", "#FF8C00", "#40E0D0", "#8A2BE2"
]

# Function to create calendar table for each month
def create_month_calendar(year, month, month_color):
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    df = pd.DataFrame(month_days, columns=days)
    df.replace(0, '', inplace=True)
    
    def style_day(val, col_name):
        if val == '':
            return ''
        elif col_name == 'Sun':
            return f'<span style="color:red">{val}</span>'
        else:
            return f'<span style="color:white">{val}</span>'

    styled_table = f'<h3 style="color:{month_color}">{calendar.month_name[month]}</h3>'
    styled_table += '<table style="border-collapse: collapse; border: 1px solid black;">'
    styled_table += '<tr>' + ''.join([f'<th style="border: 1px solid black; padding: 6px;">{d}</th>' for d in days]) + '</tr>'
    for _, row in df.iterrows():
        styled_table += '<tr>'
        for day_name, val in row.items():
            styled_table += f'<td style="border: 1px solid black; text-align: center; padding: 6px;">{style_day(val, day_name)}</td>'
        styled_table += '</tr>'
    styled_table += '</table><br>'
    return styled_table

# UI
st.title("📅 Yearly Calendar View")
year = st.selectbox("Select Year", list(range(2002, 2016)), index=0)

# Display all 12 months in grid
cols = st.columns(3)

for i in range(12):
    with cols[i % 3]:
        month_html = create_month_calendar(year, i+1, month_colors[i])
        st.markdown(month_html, unsafe_allow_html=True)