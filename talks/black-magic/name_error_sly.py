class Lexer:

    pass


class CalcLexer(Lexer):
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
