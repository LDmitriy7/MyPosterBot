from telegram import ctx
from telegram.base import BaseModel
from telegram.utils import cast


def save(context_var: str):
    context_var = context_var.lstrip('$')
    value = getattr(ctx, context_var)

    if isinstance(value, BaseModel):
        value = cast(value, dict)

    ctx.data[context_var] = value
