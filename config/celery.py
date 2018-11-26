from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', broker='redis://localhost:6379/1', backend='redis')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'exchange.tasks.get_trades',
        'schedule': 5.0,
        'args': ()
    },
}
app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()
