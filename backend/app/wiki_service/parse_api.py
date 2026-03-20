import math
from functools import reduce

class ParseWiki:
    def __init__(self):
        pass

    def parse_word_to_cite_ratio(self, api):
        try:
            data = {
                'words': api['words'],
                'characters': api['characters'],
                'sections': api['sections'],
                'citations': {
                    'total': api['references'],
                    'unique': api['unique_references']
                }
            }
            return data
        except KeyError as e:
            raise ValueError(f"Missing required key in API response: {e}")
    
    def identify_article_age(self, api):
        try:
            pages = api['query']['pages']
            if not pages:
                raise ValueError("No pages found in API response")
            page = next(iter(pages.values()))
            rev = page['revisions'][0]
            timestamp = rev['timestamp']
            comment = rev['comment']
            return {'timestamp': timestamp, 'comment': comment}
        except (KeyError, IndexError, StopIteration) as e:
            raise ValueError(f"Invalid API response structure: {e}")
    
    def recent_edits(self, api):
        try:
            pages = api['query']['pages']
            if not pages:
                return 'No pages found'
            for page in pages.values():
                revisions = page.get('revisions', [])
                if not revisions:
                    return 'No edits in the last 48 hours'
                rev_list = []
                for rev in revisions:
                    rev_data = {
                        'timestamp': rev['timestamp'],
                        'user': rev['user'],
                        'comment': rev['comment'],
                    }
                    rev_list.append(rev_data)
                return rev_list  # Returns for first page
        except KeyError as e:
            raise ValueError(f"Missing required key in API response: {e}")
        
    def registered_anonymous_and_minor_edits(self, api):
        try:
            editors = api['editors']
            anon_edits = api['anon_edits']
            minor_edits = api['minor_edits']
            modified_at = api['modified_at']
            if editors == 0 and anon_edits == 0 and minor_edits == 0:
                return {
                    'editors': 0,
                    'anon_edits': 0,
                    'minor_edits': 0,
                    'modified_at': modified_at
                }
            common_divisor = reduce(math.gcd, [editors, anon_edits, minor_edits])
            simplified_numbers = [number // common_divisor for number in [editors, anon_edits, minor_edits]]
            return {
                'editors': simplified_numbers[0],
                'anon_edits': simplified_numbers[1],
                'minor_edits': simplified_numbers[2],
                'modified_at': modified_at
            }
        except KeyError as e:
            raise ValueError(f"Missing required key in API response: {e}")
        except ZeroDivisionError:
            raise ValueError("Division by zero in simplification")
    
    def admin_cleanup(self, api):
        try:
            total_protections = len(api['protect'])
            total_unprotect_actions = 0
            last_protection = max(api['protect'], key=lambda x: x['timestamp']) if api['protect'] else None

            total_deletions = len(api['delete'])
            total_restores = 0
            last_deletion = max(api['delete'], key=lambda x: x['timestamp']) if api['delete'] else None

            total_moves = len(api['move'])

            active_admin = {}

            for unprotect in api['protect']:
                if unprotect.get('action') == 'unprotect':
                    total_unprotect_actions += 1

            for restore in api['delete']:
                if restore.get('action') == 'restore':
                    total_restores += 1

            for ltype in ['protect', 'delete', 'move']:
                for log in api[ltype]:
                    user = log.get('user')
                    if user:
                        if user in active_admin:
                            active_admin[user] += 1
                        else:
                            active_admin[user] = 1

            return {
                'total_protections': total_protections,
                'total_unprotect_protections': total_unprotect_actions,
                'last_protection': last_protection,
                'total_deletions': total_deletions,
                'total_restores': total_restores,
                'last_deletion': last_deletion,
                'total_moves': total_moves,
                'active_admin': active_admin
            }
        except KeyError as e:
            raise ValueError(f"Missing required key in API response: {e}")

    def assessment(self, api, article_name):
        new_name = article_name.replace('_', ' ')
        try:
            if new_name not in api['pages']:
                raise ValueError(f"Article '{new_name}' not found in API response")
            page = api['pages'][new_name]
            article_class = page['assessment']['class']
            article_category = page['assessment']['category']
            article_badge = page['assessment']['badge']
            article_color = page['assessment']['color']

            wikiproject_data = page['wikiprojects']

            projects = []
            for wikiproject in wikiproject_data:
                level = wikiproject_data[wikiproject]
                wikiproject_level = {
                    'name': level['wikiproject'],
                    'class': level['class']['value'],
                    'importance': level['importance']['value']
                }
                projects.append(wikiproject_level)

            data = {
                'class': article_class,
                'category': article_category,
                'badge': article_badge,
                'color': article_color,
                'projects': projects
            }

            return data
        except KeyError as e:
            raise ValueError(f"Missing required key in API response: {e}")