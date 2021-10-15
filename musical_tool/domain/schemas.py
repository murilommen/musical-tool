from typing import List, Dict
from pydantic import BaseModel


class Analysis(BaseModel):
    music: str
    group: str
    musicAnalysis: List[Dict[str, int]]
    name: str
    params: List[str]
