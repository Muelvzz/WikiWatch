import streamlit as st
import math
import plotly.express as px
import pandas as pd

def present_reg_anon(api):
    registered_edits = api.get('editors', 'N/A')
    anonymous_edits = api.get('anon_edits', 'N/A')
    minor_edits = api.get('minor_edits', 'N/A')

    try:
        gcd = math.gcd(anonymous_edits, registered_edits)

        simiplified_r = registered_edits // gcd
        simplified_a = anonymous_edits // gcd

        st.subheader(f'Registered to Anonymous edits ratio: {simiplified_r} : {simplified_a}')

    except ValueError:
        st.subheader('Registered to Anonymous edit ratio: N/A')

    try:
        data = {
            'Category': ['Registered edits', 'Anonymous edits', 'Minor Edits'],
            'Value': [registered_edits, anonymous_edits, minor_edits]
        }
        df = pd.DataFrame(data)

        fig = px.pie(df, values='Value', names='Category', title='Total Edits')

        st.plotly_chart(fig)
    except Exception as exc:
        st.error('Unable to show registered/anonymous/minor edits data.')
        st.exception(exc)
    
    st.write(f"Last Edited: {api.get('modified_at', 'N/A')}")