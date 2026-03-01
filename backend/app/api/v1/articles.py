from fastapi import APIRouter, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from ...schemas import article_schema
from ...services.wiki_calculate import analyzed_data

router = APIRouter(
    tags=['WikiWatch Analysis'],
    prefix='/analyze'
)

limiter = Limiter(key_func=get_remote_address)

@router.post('/', response_model=article_schema.DataResult)
@limiter.limit('5/minute')
async def url_analyze(request: Request, url_input: article_schema.UrlInput):

    data = analyzed_data(url_input.url_input)

    if not data:
        raise HTTPException(status_code=400, detail="Error! Something's wrong in the Backend")
    
    return data

'''
1. articles_py will send a url
2. the url will then be passed to the schema
3. the schema will then be passed to the wiki_calculate
4. the wiki_calculate will then call the wiki_fetch

5. the wiki_fetch will then request an api
6. the wiki_fetch will return it to the wiki_calcualte
7. the wiki_calculate will then analyzed the api
8. the wiki_calculate will then return the process api

9. the other schema's on artichle_schema will check the wiki_calculate process
10. the article_schema will then send it backn to the articles_py for output
'''