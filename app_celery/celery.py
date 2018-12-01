from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('app_celery',
             broker='redis://localhost:6379/1',
             backend='redis://localhost:6379/1',
             include=['app_celery.tasks'])


app.conf.beat_schedule = {
    'add-every-20-seconds': {
        'task': 'app_celery.tasks.get_trades',
        'schedule': 20.0,
        'args': ()
    },
}
app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()
