import requests, os
from urllib.parse import urlparse
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class GetData:
    def __init__(self, wiki_url):
        self.parsed_url = urlparse(wiki_url)
        self.project = self.parsed_url.netloc
        self.article = self.parsed_url.path.split('/')[-1]
        self.headers = {'User-Agent': f'MyAnalysisTool/1.0 ({os.getenv("EMAIL")})'}
        self.revert_time = (datetime.now() - timedelta(hours=48)).strftime('%Y-%m-%dT%H:%M:%SZ')

    def get_prose(self):
        prose_url = f"https://xtools.wmcloud.org/api/page/prose/{self.project}/{self.article}"

        prose_response = requests.get(prose_url, headers=self.headers)

        if prose_response.status_code == 200:
            return prose_response.json()
        else:
            return f'Failed to fetch data. Status code: {prose_response.status_code}'

    def get_article_info(self):
        article_info_url = f"https://xtools.wmcloud.org/api/page/articleinfo/{self.project}/{self.article}"

        article_info_response = requests.get(article_info_url, headers=self.headers)

        if article_info_response.status_code == 200:
            return article_info_response.json()
        else:
            return f'Failed to fetch data. Status code: {article_info_response.status_code}'

    def get_assessments(self):
        assessments_url = f"https://xtools.wmcloud.org/api/page/assessments/{self.project}/{self.article}"

        assessments_response = requests.get(assessments_url, headers=self.headers)

        if assessments_response.status_code == 200:
            return assessments_response.json()
        else:
            return f'Failed to fetch data. Status code: {assessments_response.status_code}'

    def get_reverts(self):
        revert_url = f"https://{self.project}/w/api.php"

        params = {
                "action": "query",
                "format": "json",
                "prop": "revisions",
                "titles": self.article,
                "rvprop": "timestamp|tags",
                "rvlimit": "max",     # Get as many as possible (up to 500)
                "rvend": self.revert_time     # Stop looking once we hit 48 hours ago
            }

        revert_response = requests.get(revert_url, params=params, headers=self.headers)

        if revert_response.status_code == 200:
            return revert_response.json()
        else:
            return f'Failed to fetch data. Status code: {revert_response.status_code}'

user_input = "https://en.wikipedia.org/wiki/Magnus_Carlsen"

data = GetData(user_input)

data_json = {
    'prose': data.get_prose(),
    'article_info': data.get_article_info(),
    'assessment': data.get_assessments(),
    'revert': data.get_reverts(),
}

print(data_json)