import asyncio
from datetime import datetime, timezone
from typing import List

import aiohttp
import pandas as pd
from pydantic import ValidationError

from schemas import RowModel, APIResponseModel


async def get_api_response():
    current_utc_timestamp = int(
        datetime.now(timezone.utc)
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .timestamp()
    )
    bank_url: str = "https://api.gazprombank.ru/very/important/docs?documents_date="
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{bank_url}{current_utc_timestamp}") as response:
            response.raise_for_status()
            data = await response.json()
            return data


def validate_api_response(data: dict):
    try:
        api_response = APIResponseModel(**data)
        rows_validated = [
            RowModel(key1=int(row[0]), key2=datetime.fromisoformat(row[1]), key3=row[2])
            for row in api_response.Rows
        ]
    except ValidationError as e:
        print(f"Validation error: {e}")
        raise
    return rows_validated, api_response.Columns


def transform_data_to_dataframe(
        validated_data: List[RowModel], api_response_columns: List[str]
):
    return pd.DataFrame([row.dict() for row in validated_data])


def rename_dataframe_columns(df: pd.DataFrame):
    df.rename(
        columns={"key1": "document_id", "key2": "document_dt", "key3": "document_name"},
        inplace=True,
    )


def add_load_dt_column_to_dataframe(df: pd.DataFrame):
    df["load_dt"] = datetime.now(timezone.utc)


def save_dataframe_to_csv(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)
    print(f"DataFrame saved to {file_path}")
    return file_path


async def main():
    api_response = await get_api_response()
    validated_data, api_response_columns = validate_api_response(api_response)
    df = transform_data_to_dataframe(validated_data, api_response_columns)
    rename_dataframe_columns(df)
    add_load_dt_column_to_dataframe(df)
    save_dataframe_to_csv(df, "6/output.csv")


if __name__ == "__main__":
    asyncio.run(main())
