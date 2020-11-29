from celery import Celery


celery_app = Celery('celery_tester',
                    broker='redis://:helloword@localhost:6379/0',
                    backend='redis://:helloword@localhost:6379/1')

celery_app.conf.update(task_track_started=True)
