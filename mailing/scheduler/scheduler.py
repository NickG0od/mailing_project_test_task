import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from mailing__mailing import sender as mailing_sender


class Scheduler:
    def __init__(self, instance_id=-1, run_date=None, task_id="task_1"):
        self.instance_id = instance_id
        self.run_date = run_date
        self.task_id = task_id
        self.scheduler = BackgroundScheduler(timezone=pytz.utc)
        self.scheduler.add_listener(self.scheduler_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
        self.start()

    def start(self):
        task_func = None
        if self.task_id == "task_1":
            task_func = mailing_sender.send_mailing
        elif self.task_id == "task_2":
            task_func = mailing_sender.send_to_external_api
        if task_func is None:
            return "ERROR. No task set."
        if self.run_date is not None:
            self.scheduler.add_job(task_func, replace_existing=True, trigger='date', run_date=self.run_date, args=[self.instance_id], id=self.task_id)
        else:
            self.scheduler.add_job(task_func, replace_existing=True, args=[self.instance_id], id=self.task_id)
        self.scheduler.start()

    def scheduler_listener(self, event):
        if event.exception:
            print("Scheduler execute fail")
            print("Scheduler method:", dir(self.scheduler))
        else:
            print("Scheduler execute success")
            self.scheduler.shutdown(wait=False)

