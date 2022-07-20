from telegram.handlers.base import Handler
from telegram import filters, ctx


def step(switch: str):
    if '/' not in switch:
        _at, _next = switch, ...
    else:
        _at, _next = switch.split('/', maxsplit=1)

    if _at == '':
        _at = None

    if _next == '':
        _next = None

    def deco(handler: Handler):
        index = handler.filters.index(filters.State())
        handler.filters[index] = filters.State(_at)

        if _next is not ...:
            old_func = handler.func

            def new_func():
                old_func()
                ctx.state = _next

            handler.func = new_func

        return handler

    return deco
