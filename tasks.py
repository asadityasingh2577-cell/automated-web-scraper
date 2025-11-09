from celery import Celery
from config import REDIS_URL
from scraper import scrape_and_store

celery_app = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)

celery_app.conf.beat_schedule = {
    "scrape-every-1-hour": {
        "task": "tasks.run_scrape",
        "schedule": 3600.0,
    },
}
celery_app.conf.timezone = "UTC"

@celery_app.task(name="tasks.run_scrape")
def run_scrape():
    print("Celery task: running scraper")
    count = scrape_and_store()
    return {"inserted": count}
