import redis
import logging

logging.basicConfig(level=logging.INFO)


class Redis:
    __URL = 'localhost'
    __PORT = 6379
    __redisClient = redis.StrictRedis(host=__URL, port=__PORT, decode_responses=True)

    @classmethod
    def save(cls, exchangeSymbols: str, dataPrice: dict) -> None:
        try:
            cls.__redisClient.hmset(exchangeSymbols, dataPrice)
            message = cls.__redisClient.hgetall(exchangeSymbols)
            logging.info(message)
        except Exception as error:
            logging.info(error)
