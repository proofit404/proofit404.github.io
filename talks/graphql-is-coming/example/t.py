import json
from itertools import count

from taskmanager.schema import schema

counter = count(1)


def j(request):
    num = next(counter)
    print('\n#%d\n' % num)
    result = schema.execute(request)
    print(json.dumps(result.data, indent=2))
    print(json.dumps(result.errors, indent=2))


j("""
{
  employee {
    firstName
  }
}
""")

j("""
{
  me: employee {
    firstName
  }
  employee(skip: 1) {
    firstName
  }
}
""")

j('''
query {
  task(id: 2) {
    title
  }
}
''')

j('''
query {
  tasks {
    title
  }
}
''')

j('''
{
  employees {
    firstName
  }
}
''')

j('''
{
  employees {
    firstName
    subordinates {
      firstName
    }
  }
}
''')

j('''
{
  employees {
    ...EmpAttrs
    subordinates {
      ...EmpAttrs
      subordinates {
        ...EmpAttrs
        subordinates {
          ...EmpAttrs
        }
      }
    }
  }
}

fragment EmpAttrs on Employee {
  firstName
  assignedTasks {
    title
    statusHistory {
      name
    }
    comments {
      author {
        firstName
      }
      text
    }
  }
}
''')

j('''
{
  tasks {
    title
    createdBy {
      firstName
      subordinates {
        firstName
      }
    }
  }
}
''')

j('''
{
  employees {
    firstName
  }
  tasks {
    title
  }
}
''')

j('''
{
  tasks(limit: 1) {
    title
  }
}
''')

j('''
{
  employee(id: 5) {
    firstName
    assignedTasks(limit: 1) {
      title
    }
  }
}
''')
