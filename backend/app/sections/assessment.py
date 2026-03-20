import streamlit as st
import pandas as pd

def present_assessment(api):
    try:
        if not isinstance(api, dict):
            st.write(api)
            return

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"Class: {api.get('class', 'N/A')}")
        with col2:
            st.write(f"Category: {api.get('category', 'N/A')}")

        projects = api.get('projects', [])
        if not isinstance(projects, list) or not projects:
            st.info('No wikiproject assessment data is available.')
            return

        name_col = []
        class_col = []
        importance_col = []

        for project in projects:
            name_col.append(project.get('name', 'N/A'))
            class_col.append(project.get('class', 'N/A'))
            importance_col.append(project.get('importance', 'N/A'))

        data = {
            'Name': name_col,
            'Class': class_col,
            'Importance': importance_col
        }

        df = pd.DataFrame(data)
        st.dataframe(df)

    except Exception as exc:
        st.error('Unable to display assessment data.')
        st.exception(exc)