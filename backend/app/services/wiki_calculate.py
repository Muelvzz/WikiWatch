from app.services.wiki_fetch import user_input
from app.schemas import article_schema

class AnalyzeData():
    def __init__(self, get_data):
        self.get_data = get_data

    def analyze_prose(self):
        data = self.get_data['prose']
        if isinstance(data, dict):
            words = int(data.get('words'))
            references = int(data.get('unique_references'))

            return references / words
        return data

    def analyze_article_info(self):
        data = self.get_data['article_info']
        if isinstance(data, dict):
            all_edits = int(data.get('editors'))

            anon_edits = int(data.get('anon_edits'))
            reg_edits = all_edits - anon_edits

            anon_percentage_edit = f'{(anon_edits / all_edits):.2%}'
            logged_percentage_edit = f'{(anon_edits / reg_edits):.2%}'

            contributor = {
                'anonymous': anon_percentage_edit,
                'registered': logged_percentage_edit
            }

            return contributor
        return data

    def analyze_assessment(self):
        data = self.get_data['assessment']
        if isinstance(data, dict):
            page_name = list(data['pages'].keys())[0]
            class_badge = data['pages'][page_name]['assessment'].get('class')

            return class_badge
        return data

    def analyze_reverts(self):
        data = self.get_data['revert']
        if isinstance(data, dict):
            pages_dict = data['query']['pages']
            page_id = list(pages_dict.keys())[0]
            revisions_list = pages_dict[page_id].get('revisions', [])
            revision_count = len(revisions_list)

            return revision_count
        return data
    
def analyzed_data(url_input):
    if isinstance(url_input, article_schema.UrlInput):
        url = url_input.url_input
    else:
        url = url_input

    data = user_input(url)
    analyze_data = AnalyzeData(data)
    
    prose_val = analyze_data.analyze_prose()
    assessment_val = analyze_data.analyze_assessment()
    revert_val = analyze_data.analyze_reverts()

    data_json = {
        'prose': {'prose': prose_val} if isinstance(prose_val, (int, float)) else prose_val,
        'article_info': analyze_data.analyze_article_info(),
        'assessment': {'class_badge': assessment_val} if isinstance(assessment_val, str) else assessment_val,
        'revert': {'revision_count': revert_val} if isinstance(revert_val, int) else revert_val,
    }

    return data_json