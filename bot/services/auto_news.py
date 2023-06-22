import datetime as dt

from apscheduler.jobstores.base import JobLookupError

from bot.services.tasks.daily_advices import daily_advice


class Notifier:
    def __init__(self, scheduler, bot):
        self.scheduler = scheduler
        self.job_id = None
        self.bot = bot
        self.scheduler.start()

    async def enable(self):
        job = self.scheduler.add_job(daily_advice, 'cron', args=(self.bot,), second=0)
        if self.job_id:
            await self.disable()
        self.job_id = job.id

    async def disable(self):
        if self.job_id is None:
            return
        try:
            self.scheduler.remove_job(self.job_id)
            self.job_id = None
        except JobLookupError:
            pass