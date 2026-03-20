def fetch_and_parse(url_link):
    from wiki_service.fetch_api import FetchWiki
    from wiki_service.parse_api import ParseWiki

    fetch_wiki = FetchWiki(url_link)
    parse_wiki = ParseWiki()

    parse_article = fetch_wiki.parse_article()
    project = parse_article['project']
    article = parse_article['article']
    headers = parse_article['headers']
    revert_time = parse_article['revert_time']

    fcawc = fetch_wiki.fetch_citations_and_word_count(project, article)
    pwtcr = parse_wiki.parse_word_to_cite_ratio(fcawc)

    faa = fetch_wiki.fetch_article_age(article, headers)
    iaa = parse_wiki.identify_article_age(faa)

    fre = fetch_wiki.fetch_recent_edit(revert_time, article, headers)
    re = parse_wiki.recent_edits(fre)

    # ftpa = fetch_wiki.fetch_talk_page_activity(article, headers)

    fraaame = fetch_wiki.fetch_registered_and_anonymous_and_minor_edits(project, article)
    raame = parse_wiki.registered_anonymous_and_minor_edits(fraaame)

    fac = fetch_wiki.fetch_admin_cleanup(article, headers)
    ac = parse_wiki.admin_cleanup(fac)

    fwa = fetch_wiki.fetch_wikipedia_assessment(project, article)
    a = parse_wiki.assessment(fwa, article)

    data = {
        'word_cite_ratio': pwtcr,
        'article_age': iaa,
        'edits': re,
        # 'talk_activity': ftpa,
        'anon_minor_edits': raame,
        'admin_cleanup': ac,
        'assessment': a
    }

    return data