import aiohttp
import asyncio
import aioredis
from datetime import datetime
from config.settings import CRYPTO_PAIRS


async def save_trade(pair, trade):
    date = datetime.strftime(datetime.now(), '%d.%m.%y')
    redis = await aioredis.create_redis(('localhost', 6379), encoding='utf-8')
    key = '{}::{}'.format(pair, date)
    await redis.lpush(key, trade)


async def main_loop(pair):
    session = aiohttp.ClientSession()
    async with session.ws_connect('wss://api.bitfinex.com/ws/2') as ws:
        ws.send_str('{ "event": "subscribe", "channel": "trades", "symbol": "%s"}' % pair)
        async for msg in ws:
            if msg.data == 'close':
                ws.close()
                break
            result = await ws.receive()
            if result.data.startswith('['):
                pair = pair.lower()
                await save_trade(pair, result.data)
                await asyncio.sleep(1)
                print("status OK")


loop = asyncio.get_event_loop()
tasks = [main_loop(crypto) for crypto in CRYPTO_PAIRS]
loop.run_until_complete(asyncio.wait(tasks))
