# noinspection PyUnresolvedReferences
import app
from telegram import run, on, ctx, exc


@on.message()
def check_access():
    if ctx.user_id not in [724477101]:
        raise exc.StopProcessing()


check_access.check_first = True
check_access.exclusive = False

run(parse_mode='html')
