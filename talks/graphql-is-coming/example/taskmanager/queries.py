import graphene
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Comment as CommentModel
from .models import Employee as EmployeeModel
from .models import Status as StatusModel
from .models import Task as TaskModel


class Comment(DjangoObjectType):

    class Meta:

        model = CommentModel


class Employee(DjangoObjectType):

    class Meta:

        model = EmployeeModel
        exclude_fields = ('user', 'password', 'status')


class Status(DjangoObjectType):

    class Meta:

        model = StatusModel


class Task(DjangoObjectType):

    class Meta:

        model = TaskModel


class Query(graphene.ObjectType):

    employee = graphene.Field(Employee, skip=graphene.Int(), id=graphene.Int())
    employees = graphene.List(Employee)
    task = graphene.Field(Task, id=graphene.Int())
    tasks = graphene.List(Task, limit=graphene.Int())
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_employee(self, args, context, info):

        pk = args.get('id')
        if pk:
            return EmployeeModel.objects.get(pk=pk)
        skip = args.get('skip', 0)
        return EmployeeModel.objects.all()[skip:][0]

    def resolve_employees(self, args, context, info):

        return EmployeeModel.objects.all()

    def resolve_task(self, args, context, info):

        pk = args.get('id', 1)
        return TaskModel.objects.get(pk=pk)

    def resolve_tasks(self, args, context, info):

        limit = args.get('limit')
        queryset = TaskModel.objects.all()
        if limit:
            queryset = queryset[:limit]
        return queryset
