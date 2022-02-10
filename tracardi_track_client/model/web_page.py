from typing import Any
from uuid import uuid4

from .resource import Resource


class WebPageResource(Resource):

    def __init__(self, **data: Any):

        data['type'] = 'web-page'
        data['id'] = str(uuid4())

        super().__init__(**data)
