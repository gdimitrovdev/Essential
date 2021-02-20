# Django imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# database for user's todos
class Todo(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='todos',
        null=True
    )
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date = models.DateField(null=True)

    @property
    def is_passed(self):
        if self.date < timezone.now().date():
            return True
        return False


# database for user's files
class File(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='files', null=True)
    file = models.FileField(upload_to='files/')


# model for repeating tasks that the user needs to do every day
class DailyTask(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='daily_tasks', null=True)
    text = models.CharField(max_length=200)
    last_completed = models.DateField(null=True, default=None)

    @property
    def completed_today(self):
        # if the task has never been completed
        if not self.last_completed:
            return False
        # if the task has been completed today
        if timezone.datetime.now().date() == self.last_completed:
            return True
        # if the task has been completed but not today
        return False
