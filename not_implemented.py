#!/usr/bin/env python


class MyClass(object):
    def __init__(self):
        self.my_function()

    def my_function(self):
        raise self.not_implemented()

    def not_implemented(self):
        import inspect
        fmt = 'Class {} does not implement {}()'
        caller_name = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
        return NotImplementedError(fmt.format(self.__class__.__name__,
                                              caller_name))

# --> NotImplementedError: Class MyClass does not implement my_function()
MyClass()
