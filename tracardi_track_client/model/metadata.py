from pydantic import BaseModel
from .time import Time


class Metadata(BaseModel):
    time: Time
    ip: str = None
