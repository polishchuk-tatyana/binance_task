import asyncio
from app.BinanceConsumer import Consumer


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = loop.run_until_complete(Consumer().consume(host='stream.binance.com', port=9443, streamName='!ticker@arr'))

