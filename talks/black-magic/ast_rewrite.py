import ast


class Int2Str(ast.NodeTransformer):

    def visit_Num(self, node):

        return ast.copy_location(
            ast.Str(s=str(node.n)),
            node,
        )

exp = 'c = [1, 2, 3]'

exec(exp)

print(c)

a = ast.parse(exp)

b = Int2Str().visit(a)

exec(compile(b, filename='simple.py', mode='exec'))

print(c)
