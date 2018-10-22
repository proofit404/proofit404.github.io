class Model:

    pass


class CharField:

    pass


class DateTimeField:

    pass


class Question(Model):

    question_text = CharField()
    pub_date = DateTimeField()


q = Question()
print(q.pub_date)
