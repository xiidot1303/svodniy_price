from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from scheduled_job import mailing, uploading

class jobs:
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    scheduler.add_job(mailing.send_message, 'interval', minutes=5)
    scheduler.add_job(uploading.update_excel, 'interval', minutes=5)