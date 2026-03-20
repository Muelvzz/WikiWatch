import streamlit as st
from sections.fetch_and_parse import fetch_and_parse

from sections.word_cite import present_word_cite
from sections.article_age import present_article
from sections.edits import present_edits
from sections.reg_anon_edit import present_reg_anon
# from sections.talk_activity import present_talk_activity
from sections.admin_cleanup import present_admin_cleanup
from sections.assessment import present_assessment

def present_data(api):
    word_cite_ratio = api['word_cite_ratio']
    article_age = api['article_age']
    edits = api['edits']
    # talk_activity = api['talk_activity']
    anon_minor_edits = api['anon_minor_edits']
    admin_cleanup = api['admin_cleanup']
    assessment = api['assessment']

    st.header('Basic Information')
    present_word_cite(word_cite_ratio)
    present_article(article_age)
    st.divider()

    st.header('Editors for the last 48 hours')
    present_edits(edits)
    present_reg_anon(anon_minor_edits)
    st.divider()

    # st.header('Talk Activity')
    # present_talk_activity(talk_activity)

    st.header("Admin Cleanup")
    present_admin_cleanup(admin_cleanup)
    st.divider()

    st.header('Assessment')
    present_assessment(assessment)

def main():
    import time

    st.set_page_config(
        page_title='WikiWatch Project',
        layout='wide'
    )

    st.header('WikiWatch Project')

    st.divider()

    input = st.text_input('Enter the wikipedia link', value='', width='stretch')
    input_button = st.button('Submit')

    if input_button:
        st.divider()

        api = fetch_and_parse(input)
        present_data(api)


if __name__ == "__main__":
    main()