import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='[{levelname:.1} {processName}.{threadName} {module}:{lineno}] {message}',
    style='{'
)

def f(obj):
    return f'<{type(obj).__name__} {hex(id(obj))}>'
