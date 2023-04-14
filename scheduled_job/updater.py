from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import mailing, uploading

class jobs:
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(mailing.send_message, 'interval', minutes=5)
    scheduler.add_job(uploading.update_excel, 'interval', minutes=5)