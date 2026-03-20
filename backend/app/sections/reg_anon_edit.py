import streamlit as st

def present_reg_anon(api):
    try:
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"Registered Edits: {api.get('editors', 'N/A')}")
            st.write(f"Anonymous Edits: {api.get('anon_edits', 'N/A')}")

        with col2:
            st.write(f"Minor Edits: {api.get('minor_edits', 'N/A')}")
            st.write(f"Last Edited: {api.get('modified_at', 'N/A')}")
    except Exception as exc:
        st.error('Unable to show registered/anonymous/minor edits data.')
        st.exception(exc)