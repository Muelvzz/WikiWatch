import os, requests
from urllib.parse import urlparse
from datetime import datetime, timedelta
from dotenv import load_dotenv

class FetchWiki:
    def __init__(self, article_link):
        self.__article_link = article_link

    def get_article_name(self):
        return self.__article_link
    
    def parse_article(self, article_link=None):
        if article_link is None:
            article_link = self.get_article_name()

        parsed_url = urlparse(article_link)
        project = parsed_url.netloc
        article = parsed_url.path.split('/')[-1]
        headers = {'User-Agent': f'MyAnalysisTool/1.0({os.getenv('EMAIL')})'}
        revert_time = (datetime.now() - timedelta(hours=48)).strftime('%Y-%m-%dT%H:%M:%SZ')

        url_parse = {
            'project': project,
            'article': article,
            'headers': headers,
            'revert_time': revert_time
        }

        return url_parse
    
    def fetch_citations_and_word_count(self, project_name, article_name):
        url = f"https://xtools.wmcloud.org/api/page/prose/{project_name}/{article_name}"
        response = requests.get(url)
        data = response.json()

        return data
    
    def fetch_article_age(self, article_name, headers):
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "prop": "revisions",
            "rvlimit": 1,
            "rvdir": "newer",
            "titles": article_name,
            "format": "json"
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def fetch_recent_edit(self, timestamp, article_name, headers):
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "prop": "revisions",
            "rvlimit": 1,
            "rvend": timestamp,
            "rvdir": "older",
            "rvprop": "timestamp|user|comment",
            "titles": article_name,
            "format": "json"
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def fetch_talk_page_activity(self, article_name, headers):
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "titles": f'Talk:{article_name}',
            "prop": "info",
            "format": "json"
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def fetch_registered_and_anonymous_ratio(self, project_name, article_name):
        url = f'https://xtools.wmcloud.org/api/page/articleinfo/{project_name}/{article_name}'
        response = requests.get(url)
        data = response.json()

        return data
    
    def fetch_admin_cleanup(self, article_name, headers):
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "logevents",
            "letitle": article_name,
            "format": "json"
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def fetch_wikipedia_assessment(self, project_name, article_name):
        url = f'https://xtools.wmcloud.org/api/page/assessments/{project_name}/{article_name}'
        response = requests.get(url)
        data = response.json()

        return data

# if __name__ == '__main__':
#     fetch_wiki = FetchWiki('https://en.wikipedia.org/wiki/Naruto')
#     parsed_article = fetch_wiki.parse_article()

#     project = parsed_article['project']
#     article = parsed_article['article']
#     headers = parsed_article['headers']
#     revert_time = parsed_article['revert_time']

#     url_data = fetch_wiki.fetch_wikipedia_assessment(project, article)

#     print(url_data)