from .app import celery_app
from service import item as item_service
import time


@celery_app.task(acks_late=True)
def get_item_price(item_id: int) -> float:
    item = item_service.get_item(item_id)
    time.sleep(3)
    if not item:
        return -1.0
    return item.price
