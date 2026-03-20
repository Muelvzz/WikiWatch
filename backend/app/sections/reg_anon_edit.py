import streamlit as st

def present_reg_anon(api):
    col1, col2 = st.columns(2)

    with col1:
        st.write(f'Registered Edits: {api['editors']}')
        st.write(f'Anonymous Edits: {api['anon_edits']}')

    with col2:
        st.write(f'Minor Edits: {api['minor_edits']}')
        st.write(f'Last Edited: {api['modified_at']}')