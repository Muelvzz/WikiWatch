import streamlit as st
from datetime import datetime

def present_article(api):
    timestamp = api['timestamp']
    comment = api['comment']

    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = dt.strftime("%B %d, %Y at %I:%M %p")

    st.write(f'Created: {formatted_date}')
    st.write(f'Comment: {comment}')
