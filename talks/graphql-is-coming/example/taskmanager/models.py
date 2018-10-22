from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Task(models.Model):

    title = models.CharField(max_length=300)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_tasks',
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_tasks',
    )

    class Meta:

        verbose_name = 'task'
        verbose_name_plural = 'tasks'


class Status(models.Model):

    name = models.CharField(
        max_length=1,
        choices=[
            ('n', 'new'),
            ('s', 'started'),
            ('c', 'completed'),
            ('r', 'rejected'),
        ],
        default='n',
    )
    task = models.ForeignKey('Task', related_name='status_history')
    date = models.DateTimeField(default=timezone.now)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:

        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
    )
    task = models.ForeignKey('Task', related_name='comments')
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    class Meta:

        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Employee(AbstractUser):

    chief = models.ForeignKey('self', related_name='subordinates', null=True)

    class Meta:

        verbose_name = 'employee'
        verbose_name_plural = 'employees'
