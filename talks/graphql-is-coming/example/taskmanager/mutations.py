import graphene

from .models import Employee as EmployeeModel
from .models import Task as TaskModel
from .queries import Task


class CreateTask(graphene.Mutation):

    class Input:

        title = graphene.String()
        description = graphene.String()
        assigned_to = graphene.String()

    task = graphene.Field(Task)

    @staticmethod
    def mutate(root, args, context, info):

        title = args.get('title')
        description = args.get('description')
        assigned_username = args.get('assigned_to')
        executor = EmployeeModel.objects.get(username=assigned_username)
        creator = context.user
        task = TaskModel.objects.create(
            title=title,
            description=description,
            assigned_to=executor,
            created_by=creator,
        )
        return CreateTask(task=task)


class Mutation(graphene.ObjectType):

    create_task = CreateTask.Field()
