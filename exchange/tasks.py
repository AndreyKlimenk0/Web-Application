import celery


app = celery.Celery('tasks', broker='redis://localhost:6379/0', backend='redis')


@app.task
def add(x, y):
    return x + y
