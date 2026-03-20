import streamlit as st
from datetime import datetime

def present_article(api):
    try:
        timestamp = api.get('timestamp')
        comment = api.get('comment')

        if not timestamp:
            raise ValueError('Article age timestamp is missing.')

        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = dt.strftime("%B %d, %Y at %I:%M %p")

        st.write(f'Created: {formatted_date}')
        st.write(f'Comment: {comment}')
    except Exception as exc:
        st.error('Unable to present article age.')
        st.exception(exc)
