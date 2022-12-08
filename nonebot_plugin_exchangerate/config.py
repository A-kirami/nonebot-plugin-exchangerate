from nonebot import get_driver
from pydantic import BaseModel, Extra, Field


class Config(BaseModel, extra=Extra.ignore):
    exchange_app_key: str
    exchange_decimals: int = Field(2, ge=0)


config = Config.parse_obj(get_driver().config)
