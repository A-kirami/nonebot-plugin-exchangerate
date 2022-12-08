from datetime import datetime
from typing import Dict, List, Tuple

import httpx
from nonebot import require
from nonebot.log import logger
from pydantic import BaseModel

from .config import config

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler

currency_dict: Dict[str, Tuple[str, ...]] = {
    "澳大利亚元": ("澳元",),
    "加拿大元": ("加元", "加币"),
    "瑞士法郎": ("法郎",),
    "丹麦克朗": (),
    "欧元": (),
    "英镑": (),
    "港币": ("港元", "香港元"),
    "印尼卢比": (),
    "日元": ("円", "日圆"),
    "韩元": ("韩币",),
    "澳门元": ("澳币", "澳门币"),
    "挪威克朗": (),
    "新西兰元": (),
    "菲律宾比索": ("比索",),
    "卢布": ("俄元",),
    "瑞典克朗": (),
    "新加坡元": (),
    "泰国铢": ("泰铢",),
    "土耳其里拉": (),
    "美元": ("美刀",),
    "南非兰特": (),
}


class ExchangeRate(BaseModel):
    name: str
    """货币名称"""
    unit: int
    """交易单位"""
    spot_exchange: float
    """现汇买入价"""
    cash_purchase: float
    """现钞买入价"""
    cash_sellout: float
    """现钞卖出价"""
    conversion: float
    """中行折算价"""

    def exchange(self, amount: float) -> float:
        """CNY兑换外币"""
        sums = self.cash_sellout / self.unit * amount
        if config.exchange_decimals:
            return round(sums, config.exchange_decimals)
        return round(sums)


fields = ExchangeRate.__fields__.keys()

exchange_dict: Dict[str, ExchangeRate] = {}

update_time = ""


@scheduler.scheduled_job(
    "interval", minutes=30, args=[config.exchange_app_key], next_run_time=datetime.now()
)
async def fetch_exchange(app_key: str) -> None:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"http://op.juhe.cn/onebox/exchange/query?key={app_key}"
        )
    result = response.json()["result"]
    currency_list = result["list"]
    global exchange_list
    exchange_dict.clear()
    for currency in currency_list:
        params = dict(zip(fields, currency))
        exchange_dict[currency[0]] = ExchangeRate(**params)
    global update_time
    update_time = result["update"]
    logger.debug(f"汇率更新成功! 更新时间: {update_time}")


def get_exchangerate(name: str) -> ExchangeRate:
    try:
        return exchange_dict[name]
    except KeyError:
        for k, v in currency_dict.items():
            if name in v:
                return exchange_dict[k]
    raise ValueError("查找的货币不存在")


def exchange_currency(name: str, amount: float) -> float:
    er = get_exchangerate(name)
    return er.exchange(amount)


def get_currency_info(name: str) -> str:
    er = get_exchangerate(name)
    return (
        f"货币名称: {er.name}\n"
        f"现汇买入价: {er.spot_exchange}\n"
        f"现钞买入价: {er.cash_purchase}\n"
        f"现钞卖出价: {er.cash_sellout}\n"
        f"中行折算价: {er.conversion}\n"
        f"更新时间: {update_time}"
    )


def get_currency_list() -> List[str]:
    return list(exchange_dict.keys())
