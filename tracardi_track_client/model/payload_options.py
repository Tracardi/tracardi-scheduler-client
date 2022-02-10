from pydantic import BaseModel


class PayloadOptions(BaseModel):
    profile: bool = False
