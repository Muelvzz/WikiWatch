import streamlit as st
import pandas as pd

def present_edits(api):
    try:
        if isinstance(api, str):
            st.write(api)
            return

        timestamp_col = []
        user_col = []
        comment_col = []

        for page in api:
            timestamp_col.append(page.get('timestamp', ''))
            user_col.append(page.get('user', ''))
            comment_col.append(page.get('comment', ''))

        data = {
            'Timestamp': timestamp_col,
            'User': user_col,
            'Comment': comment_col,
        }

        df = pd.DataFrame(data)
        st.dataframe(df)
    except Exception as exc:
        st.error('Unable to show recent edits data.')
        st.exception(exc)