import streamlit as st
import math

def present_word_cite(api):
    try:
        words = api.get('words')
        characters = api.get('characters')
        sections = api.get('sections')
        citations = api.get('citations', {})
        total = citations.get('total')
        unique = citations.get('unique')

        gcd = math.gcd(total, words)
        simplified_word = words // gcd
        simplified_citation = total // gcd

        st.subheader(f'Citations-to-Words ratio: {simplified_citation} : {simplified_word}')
        with st.expander('Additional Information'):
            st.write(f'Word Total: {words}')
            st.write(f'Sections: {sections}')
            st.write(f'Total Links: {total}')
            st.write(f'Unique Links: {unique}')

    except Exception as exc:
        st.error('Unable to show word/cite ratios.')
        st.exception(exc)