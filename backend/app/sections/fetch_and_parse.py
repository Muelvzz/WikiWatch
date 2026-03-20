def fetch_and_parse(url_link, email):
    from wiki_service.fetch_api import FetchWiki
    from wiki_service.parse_api import ParseWiki

    if not url_link or not url_link.strip():
        raise ValueError('Wikipedia URL cannot be empty.')

    if not email or '@' not in email:
        raise ValueError('A valid email address is required.')

    try:
        fetch_wiki = FetchWiki(url_link.strip(), email.strip())
        parse_wiki = ParseWiki()

        parse_article = fetch_wiki.parse_article()
        if not isinstance(parse_article, dict) or 'error' in parse_article:
            raise ValueError(parse_article.get('error', 'Could not parse wiki link.'))

        project = parse_article['project']
        article = parse_article['article']
        headers = parse_article['headers']
        revert_time = parse_article['revert_time']

        fcawc = fetch_wiki.fetch_citations_and_word_count(project, article)
        if isinstance(fcawc, dict) and 'error' in fcawc:
            raise ValueError(fcawc['error'])
        pwtcr = parse_wiki.parse_word_to_cite_ratio(fcawc)

        faa = fetch_wiki.fetch_article_age(article, headers)
        if isinstance(faa, dict) and 'error' in faa:
            raise ValueError(faa['error'])
        iaa = parse_wiki.identify_article_age(faa)

        fre = fetch_wiki.fetch_recent_edit(revert_time, article, headers)
        if isinstance(fre, dict) and 'error' in fre:
            raise ValueError(fre['error'])
        re = parse_wiki.recent_edits(fre)

        fraaame = fetch_wiki.fetch_registered_and_anonymous_and_minor_edits(project, article)
        if isinstance(fraaame, dict) and 'error' in fraaame:
            raise ValueError(fraaame['error'])
        raame = parse_wiki.registered_anonymous_and_minor_edits(fraaame)

        fac = fetch_wiki.fetch_admin_cleanup(article, headers)
        if isinstance(fac, dict) and 'error' in fac:
            raise ValueError(fac['error'])
        ac = parse_wiki.admin_cleanup(fac)

        fwa = fetch_wiki.fetch_wikipedia_assessment(project, article)
        if isinstance(fwa, dict) and 'error' in fwa:
            raise ValueError(fwa['error'])
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

    except Exception as exc:
        raise RuntimeError(f'Error fetching and parsing wiki data: {exc}') from exc