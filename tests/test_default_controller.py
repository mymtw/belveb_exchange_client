# coding: utf-8

import pytest
import json
from aiohttp import web

from belveb_exchange_client.models.rate import Rate


async def test_get_rates_get(client):
    """Test case for get_rates_get

    Bel VEB exchange rates client
    """
    params = [('exchangeType', 'exchange_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/exchange/1/getRates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

