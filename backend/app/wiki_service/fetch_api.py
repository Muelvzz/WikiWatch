import requests
from urllib.parse import urlparse
from datetime import datetime, timedelta
from dotenv import load_dotenv

class FetchWiki:

    error_message = {'error': 'Could not fetch necessary data'}

    def __init__(self, article_link, email):
        self.__article_link = article_link
        self.__email = email

    def get_article_name(self):
        return self.__article_link
    
    def get_email(self):
        return self.__email
    
    def parse_article(self, article_link=None):
        if article_link is None:
            article_link = self.get_article_name()

        try:
            parsed_url = urlparse(article_link)
            project = parsed_url.netloc
            article = parsed_url.path.split('/')[-1]
            headers = {'User-Agent': f'MyAnalysisTool/1.0({self.get_email})'}
        
        except Exception:
            return {'error': 'Could not parse the link.'}

        else:
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

        try:
            response = requests.get(url)
            data = response.json()

            return data
        
        except requests.RequestException:
            return self.error_message
    
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

        try:
            response = requests.get(url, headers=headers, params=params)
            return response.json()
        
        except requests.RequestException:
            return self.error_message

    def fetch_recent_edit(self, timestamp, article_name, headers):
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "prop": "revisions",
            "rvlimit": 'max',
            "rvstart": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "rvend": timestamp,
            "rvdir": "older",
            "rvprop": "timestamp|user|comment",
            "titles": article_name,
            "format": "json"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            return response.json()
        
        except requests.RequestException:
            return self.error_message

    # def fetch_talk_page_activity(self, article_name, headers):
    #     url = "https://en.wikipedia.org/w/api.php"

    #     params = {
    #         "action": "query",
    #         "prop": "revision",
    #         "titles": f'Talk:{article_name}',
    #         "rvlimit": 10,
    #         "rvprop": "timestamp|user|comment",
    #         "format": "json"
    #     }

    #     try:
    #         response = requests.get(url, headers=headers, params=params)
    #         return response.json()
        
    #     except requests.RequestException:
    #         return self.error_message
    
    def fetch_registered_and_anonymous_and_minor_edits(self, project_name, article_name):
        url = f'https://xtools.wmcloud.org/api/page/articleinfo/{project_name}/{article_name}'

        try:
            response = requests.get(url)
            data = response.json()
            return data
        
        except requests.RequestException:
            return self.error_message
    
    def fetch_admin_cleanup(self, article_name, headers):
        admin = {}
        url = "https://en.wikipedia.org/w/api.php"

        log_types = ["protect", "delete", "move"]

        try:
            for ltype in log_types:
                params = {
                    "action": "query",
                    "list": "logevents",
                    "letitle": article_name,
                    "letype": ltype,
                    "lelimit": 10,
                    "format": "json"
                }
                response = requests.get(url, headers=headers, params=params)

                events = response.json().get('query', {}).get('logevents', [])
                admin[ltype] = events
        
        except requests.RequestException:
            return self.error_message
        
        return admin
    
    def fetch_wikipedia_assessment(self, project_name, article_name):
        url = f'https://xtools.wmcloud.org/api/page/assessments/{project_name}/{article_name}'

        try:
            response = requests.get(url)
            data = response.json()

            return data
        
        except requests.RequestException:
            return self.error_message