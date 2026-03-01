from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi import Limiter

from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import articles

app = FastAPI(
    title='WikiWatch',
    version='1.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.include_router(articles.router)