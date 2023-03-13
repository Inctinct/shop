import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTING_MODULE", "shop.settings")
app = Celery("shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every' : {
        'task' : 'api.tasks.get_products_statistic',
        'schedule' : crontab(),
    },
    'every' : {
            'task' : 'api.tasks.get_producer_statistic',
            'schedule' : crontab(),
        },
    'every' : {
                'task' : 'api.tasks.get_category_statistic',
                'schedule' : crontab(),
            },

}