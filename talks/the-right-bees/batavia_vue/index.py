import dom

Vue = dom.window.self.Vue


class Options:
    pass


options = Options()
options.el = '#app'
options.data = Options()
options.data.message = 'Hello Vue!'

app = Vue(options)
