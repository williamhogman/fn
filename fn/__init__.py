import sys

from fn.tracer import Tracer

class Module(object):
    def __init__(self, tracer):
        self._tracer = tracer

    @property
    def x(self):
        return self._tracer()

    def __repr__(self):
        return "fn"

    __str__ = __repr__

m = Module(Tracer)

sys.modules[__name__] = m
