import toga


def button_handler(widget):
    print("hello")


def build(app):
    box = toga.Box()
    button = toga.Button('Hello world', on_press=button_handler)
    button.style.set(margin=50)
    box.add(button)
    return box


if __name__ == '__main__':
    app = toga.App('Try App', 'org.proofit404.try_toga', startup=build)
    app.main_loop()
