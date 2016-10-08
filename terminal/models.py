from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    """This class will represent the logic of what a student should contain.
        * student_id - identifier to log to the system.
        * password - also for logging.
        * name
        * color_setting - for later use of creating themes.
        * tasks - list of tasks that belong to the user.
    """

    student_id = models.CharField(max_length=200)  # until login is enabled.
    password = models.CharField(max_length=20)  # until login is enabled.
    name = models.CharField(max_length=50)
    # tasks =


class Task(models.Model):
    """This will contain all the elevant data about a task
        * task_name - the name of the task to do.
        * task_desc - the description of the task.
        * date_created - the date the task was ceated.
        * owner - the student that this task belongs to.
    """

    NEW_TASK = "new"
    TASK_DONE = "done"
    IN_PROCESS = "in process"

    task_name = models.CharField(max_length=20)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField('task creation date')
    task_state = models.CharField(max_length=20, default=NEW_TASK)
    task_owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def is_new_task(self):
        """Check if the task is new."""
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

    def change_task_state(self, new_state):
        """Change the state of the task to the new state.

        Args:
            new_state (string): the new state of the task.
        """
        self.task_state = new_state

