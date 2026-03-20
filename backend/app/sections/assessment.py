import streamlit as st
import pandas as pd

def present_assessment(api):
    col1, col2 = st.columns(2)

    with col1:
        st.write(f'Class: {api['class']}')
    with col2:
        st.write(f'{api['category']}')

    name_col = []
    class_col = []
    importance_col = []

    for project in api['projects']:
        name_col.append(project['name'])
        class_col.append(project['class'])
        importance_col.append(project['importance'])

    data = {
        'Name': name_col,
        'Class': class_col,
        'Importance': importance_col
    }

    df = pd.DataFrame(data)
    st.dataframe(df)