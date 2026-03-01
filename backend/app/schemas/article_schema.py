from pydantic import BaseModel, Field

class UrlInput(BaseModel):
    url_input : str = Field(..., pattern=r'^https://')


class AnalyzeProse(BaseModel):
    prose: float


class AnalyzeArticleInfo(BaseModel):
    anonymous: str
    registered: str


class AnalyzeAssessment(BaseModel):
    class_badge: str


class AnalyzeRevert(BaseModel):
    revision_count: int


class DataResult(BaseModel):
    prose: AnalyzeProse
    article_info: AnalyzeArticleInfo
    assessment: AnalyzeAssessment
    revert: AnalyzeRevert

    class Config:
        from_attributes = True