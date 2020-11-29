# fastapi-celery-test

test celery with [start-fastapi](https://github.com/utmhikari/start-fastapi)


## usage

```bash
# cd to root directory
source ./venv/bin/activate
celery -A service.celery.worker worker -l info

# then run main.py and curl http://127.0.0.1:8000/v1/test/celery
```