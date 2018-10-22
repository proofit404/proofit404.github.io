import colosseum
import pyjade
import toga

index = open('index.jade').read()

ast = pyjade.Parser(index).parse()


def build(nodes, parent=None):
    for node in nodes:
        cls = getattr(toga, node.name)
        kwargs = {}
        for attr in node._attrs:
            arg = handlers[attr['name']](attr['val'])
            kwargs[attr['name']] = arg
        widget = cls(**kwargs)
        if parent:
            parent.add(widget)
        if node.block:
            build(node.block.nodes, widget)
    if parent is None:
        return widget


def get_style(style_declaration):

    style = parse(style_declaration)
    return colosseum.CSS(**style)


def parse(style):

    return {
        k: int(v)
        for k, v in (x.split(':') for x in get_text(style).split(';'))
    }


def get_function(name):

    return globals()[name]


def get_text(txt):

    return txt[1:-1]


handlers = {
    'style': get_style,
    'on_press': get_function,
    'label': get_text,
}


def button_handler(widget):
    print('hello')


def buildapp(app):

    return build(ast.nodes)


if __name__ == '__main__':
    app = toga.App('App Jade', 'org.proofit404.toga_jade', startup=buildapp)
    app.main_loop()
