import streamlit as st
import pandas as pd

def present_edits(api):
    if isinstance(api, str):
        st.write(api)
    else:
        timestamp_col = []
        user_col = []
        comment_col = []

        for page in api:

            timestamp_col.append(page['timestamp'])
            user_col.append(page['user'])
            comment_col.append(page['comment'])

        data = {
            'Timestamp': timestamp_col,
            'User': user_col,
            'Comment': comment_col,
        }

        df = pd.DataFrame(data)
        st.dataframe(df)