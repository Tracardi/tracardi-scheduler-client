from typing import List

from pydantic import BaseModel


class Operation(BaseModel):
    new: bool = False
    update: bool = False
    segment: bool = False
    merge: List[str] = []
