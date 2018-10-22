from django.contrib import admin

from .models import Comment, Employee, Status, Task

admin.site.register([Comment, Employee, Status, Task])
