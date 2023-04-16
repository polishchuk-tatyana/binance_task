import aiohttp
import logging
from app.config.RedisConfiguration import Redis

logging.basicConfig(level=logging.INFO)


class Consumer:

    @classmethod
    async def consume(cls, host: str, port: int, streamName: str) -> None:

        url = f"wss://{host}:{port}/ws/{streamName}"

        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(url) as response:
                async for message in response:

                    if message.type == aiohttp.WSMsgType.TEXT:

                        response_list = await response.receive_json()
                        for data in response_list:
                            binanceExchangeData = dict()
                            binanceExchangeData["timestamp"] = int(data['E'])
                            binanceExchangeData["last_price"] = float(data['c'])
                            exchangeSymbols = "binance:" + data['s']
                            Redis.save(exchangeSymbols, binanceExchangeData)

                    elif message.type == aiohttp.WSMsgType.CLOSED:
                        logging.info('CLOSED')
                        break

                    elif message.type == aiohttp.WSMsgType.ERROR:
                        logging.info('Error')
                        break
