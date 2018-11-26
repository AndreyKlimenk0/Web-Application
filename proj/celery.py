from celery import Celery


app = Celery('proj', broker='redis://localhost:6379/0', backend='redis')


if __name__ == '__main__':
    app.start()
