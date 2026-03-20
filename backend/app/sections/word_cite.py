import streamlit as st

def present_word_cite(api):
    try:
        words = api.get('words')
        characters = api.get('characters')
        sections = api.get('sections')
        citations = api.get('citations', {})
        total = citations.get('total')
        unique = citations.get('unique')

        col1, col2 = st.columns(2)

        with col1:
            st.write(f'Word Total: {words}')
            st.write(f'Character Total: {characters}')

        with col2:
            st.write(f'Sections: {sections}')
            st.write(f'Total Links: {total}')
            st.write(f'Unique Links: {unique}')
    except Exception as exc:
        st.error('Unable to show word/cite ratios.')
        st.exception(exc)