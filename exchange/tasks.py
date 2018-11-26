import redis
from celery import shared_task
from exchange.models import Trade


@shared_task
def get_trades():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    for key in r.keys():
        while r.exists(key):
            trade = r.rpop(key)
            trade = eval(trade)  # convert '[649, 'tu', [315073922, 1542812970215, 0.5, 4579]]' in list
            print(trade[2][0], trade[2][1], trade[0])
            save_d = Trade(amount=trade[2][0], price=trade[2][1], time=trade[0])
            save_d.save()


get_trades()
