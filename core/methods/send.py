import re

from telegram import bot, objects, ctx


def send(obj: str, kb: list[list[str]] = None, to: int | str = None, caption: str = None):
    if kb:
        if hasattr(kb, '__iter__'):
            buttons = kb
            kb = objects.Keyboard()
            for row in buttons:
                kb.add_row(*row)

    if caption:  # convert MD to html
        caption = re.sub(r'\[(.+)]\((.+)\)', r'<a href="\2">\1</a>', caption)
        caption = re.sub(r'<a href="@(.+)">(.+)</a>', r'<a href="https://t.me/\1">\2</a>', caption)

    if obj == '&photo':
        bot.send_photo(ctx.data['photo']['file_id'], reply_markup=kb, chat_id=to, caption=caption)
    else:
        bot.send_message(obj, reply_markup=kb, chat_id=to)
