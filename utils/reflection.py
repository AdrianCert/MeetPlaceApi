import inspect

def class_attributes(cls, show_private = True):
    attributes = inspect.getmembers(cls, lambda a:not(inspect.isroutine(a)))
    f_isprivate = lambda x: x.startswith('__') and x.endswith('__')
    return [a for a in attributes if show_private and not f_isprivate(a[0])]

def class_annotations(cls):
    return cls.__dict__['__annotations__']