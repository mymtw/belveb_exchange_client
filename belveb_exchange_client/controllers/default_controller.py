from typing import List, Dict
from aiohttp import web

from belveb_exchange_client.models.rate import Rate
from belveb_exchange_client import util


async def get_rates_get(request: web.Request, exchange_type) -> web.Response:
    """Bel VEB exchange rates client

    

    :param exchange_type: 
    :type exchange_type: str

    """
    return web.Response(status=200)
