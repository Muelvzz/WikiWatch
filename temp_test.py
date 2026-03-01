from app.services.wiki_calculate import analyzed_data
from app.schemas import article_schema

data = analyzed_data('https://en.wikipedia.org/wiki/Magnus_Carlsen')
print(data)
print(article_schema.DataResult(**data))
