from pydantic import BaseModel
from typing import List, Dict


class ApplyChangesRequest(BaseModel):
    resume_text: str
    suggestions: List[Dict]