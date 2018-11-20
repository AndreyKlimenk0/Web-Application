import redis
# from .celery import app
# from exchange.models import Trade
from config.settings import CRYPTO_PAIRS


def get_trades():
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, encoding='utf-8')
    for pair in CRYPTO_PAIRS:
        print(pair, r.hscan(pair.lower()))


def added_tardes():
    pass


if  __name__ == '__main__':
   get_trades()

