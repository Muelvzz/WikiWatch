import streamlit as st

def present_word_cite(api):
    words = api['words']
    characters = api['characters']
    sections = api['sections']
    total = api['citations']['total']
    unique = api['citations']['total']

    col1, col2 = st.columns(2)

    with col1:
        st.write(f'Word Total: {words}')
        st.write(f'Character Total: {characters}')

    with col2:
        st.write(f'Sections: {sections}')
        st.write(f'Total Links: {total}')
        st.write(f'Unique Links: {unique}')