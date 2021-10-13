from typing import List
from pydantic import BaseModel


class BaseOrm(BaseModel):
    class Config:
        orm_mode = True


class Analysis(BaseOrm):
    user_name: str
    user_group: str
    param_low: str
    param_high: str
    id_music: int


class Music(BaseOrm):
    music_name: str


class Time(BaseOrm):
    id_analysis: int
    timestamp: int
    value: float


class AnalysisRequest(BaseOrm):
    group: str
    music: str
    musicAnalysis: List[dict]
    name: str
    params: List[str]
