from viztracer import VizTracer

def performance(path = None):
    def decorator(funct):
        def wrapper(*args, **kwargs):
            with VizTracer(output_file=path) as tracer:
                return funct(*args, **kwargs)
        return wrapper
    return decorator