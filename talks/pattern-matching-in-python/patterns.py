# TODO:
# * tree example
# * ordered search for signatures (not for loop)


import itertools
import sys
import types


def match(*expressions):

    def decorator(f):
        if f.__name__ not in f.__globals__:
            def wrapper(*args):
                for signature, f in wrapper.signatures:
                    if signature == args:
                        return f(*signature.arguments(args))
                else:
                    raise Exception('Can not find appropriate pattern')
            wrapper.signatures = []
        else:
            wrapper = f.__globals__[f.__name__]

        signature = Signature(*expressions)
        wrapper.signatures.append((signature, f))
        return wrapper

    return decorator


class Signature:

    def __init__(self, *args):

        self.args = args

    def __eq__(self, args):

        return args == self.signature

    @property
    def predicates(self):
        def getkey(predicate):
            if hasattr(predicate, 'name'):
                return predicate.name
        return [(key, tuple(ps))
                for key, ps in itertools.groupby(self.args, getkey)]

    @property
    def signature(self):

        sign = ()
        for key, predicates in self.predicates:
            if len(predicates) == 1:
                sign += (predicates[0],)
            elif (len(predicates) == 2 and
                  isinstance(predicates[0], IndexPredicate) and
                  isinstance(predicates[1], SlicePredicate)):
                sign += (HeadTailPredicate(key, predicates[0].args[0]),)
            elif (len(predicates) > 1 and
                  all(map(lambda p: isinstance(p, Expression), predicates))):
                sign += predicates
            else:
                raise Exception('Can not interpret predicates')

        return sign

    def arguments(self, args):

        call = ()
        for s in self.signature:
            arg, args = args[0], args[1:]
            if isinstance(s, HeadTailPredicate):
                call += (arg[s.args[0]], arg[s.args[0] + 1:])
            else:
                call += (arg,)
        return call


class Expression:

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return '<{klass} {name}>'.format(
            klass=self.__class__.__name__,
            name=self.name)

    def __gt__(self, other):

        return GreaterPredicate(self.name, other)

    def __getitem__(self, item):

        if isinstance(item, int):
            return IndexPredicate(self.name, item)
        elif isinstance(item, slice):
            return SlicePredicate(self.name, item)
        else:
            raise Exception('Can not find predicate for item')

    def __eq__(self, other):

        return True


class Predicate:

    def __init__(self, name, *args):

        self.name = name
        self.args = args

    def __repr__(self):

        return '<{klass} {name}{args}>'.format(
            klass=self.__class__.__name__,
            name=self.name,
            args=self.args)


class GreaterPredicate(Predicate):

    def __eq__(self, other):

        return isinstance(other, type(self.args[0])) and other > self.args[0]


class HeadTailPredicate(Predicate):

    def __eq__(self, other):

        return isinstance(other, list) and len(other) >= self.args[0] + 1


class IndexPredicate(Predicate):

    pass


class SlicePredicate(Predicate):

    pass


class module(types.ModuleType):

    def __getattr__(self, name):

        if name == 'match':
            return match
        else:
            return Expression(name)


old_module = sys.modules['patterns']

new_module = sys.modules['patterns'] = module('patterns')
