class LexerType(type):

    @staticmethod
    def __prepare__(cls, *args, **kwargs):

        d = {}
        def _(pattern):
            def decorate(f):
                return f
            return decorate
        d['_'] = _
        return d


class Lexer(metaclass=LexerType):

    pass


class CalcLexer(Lexer):
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t


class T:

    pass


t = T()
t.value = '1'
CalcLexer().NUMBER(t)
print(type(t.value))
