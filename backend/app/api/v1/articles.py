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