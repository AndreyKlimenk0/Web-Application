import redis
from exchange.models import Trade
from app_celery.celery import app


@app.task
def get_trades():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    for key in r.keys():
        while r.exists(key):
            trade = r.rpop(key)
            trade = eval(trade)  # convert '[649, 'tu', [315073922, 1542812970215, 0.5, 4579]]' in list
            Trade(amount=trade[2][0], price=trade[2][1], time=trade[0]).save()
