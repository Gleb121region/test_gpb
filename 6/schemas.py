from datetime import datetime
from typing import List

from pydantic import BaseModel


class RowModel(BaseModel):
    key1: int
    key2: datetime
    key3: str


class APIResponseModel(BaseModel):
    Columns: List[str]
    Description: str
    RowCount: int
    Rows: List[List[str]]
