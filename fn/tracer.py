from operator import attrgetter, methodcaller

def _identity(x):
    return x

def compose(f, g):
    def fn(*args, **kwargs):
        return g(f(*args, **kwargs))
    fn.__str__ = lambda *args, **kwargs: "compose({}, {})".format(repr(f), repr(g))
    return fn

class Tracer(object):
    __slots__ = ("_tracer", )

    def __init__(self, fn=_identity):
        self._tracer = fn

    def __getattribute__(self, name):
        if name == "_tracer" or "__" in name:
            return super(Tracer, self).__getattribute__(name)
        else:
            t = self._tracer 
            return Tracer(compose(t, attrgetter(name)))

    def __call__(self, *args, **kwargs):
        return self._tracer(*args, **kwargs)
