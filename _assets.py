from __future__ import annotations

import re

import telegram
import kbs
from telegram import bot, ctx


def save(var: str, alias: str = None):
    var = var.lstrip('$')
    ctx.data[alias or var] = getattr(ctx, var)


def step(*_):
    def deco(func):
        return func

    return deco


def send(text: str, kb: str = None, **kwargs):
    if kb:
        kb_buttons = getattr(kbs, kb.lstrip('@'))
        kb = telegram.objects.Keyboard()

        for row in kb_buttons:
            kb.add_row(*row)

    bot.send_message(
        text,
        reply_markup=kb,
    )


def send_photo(photo: str, caption: str = None, to: int | str = None):
    if photo.startswith('&'):
        photo = ctx.data[photo.lstrip('&')]

    if caption:  # convert MD to html
        caption = re.sub(r'\[(.+)]\((.+)\)', r'<a href="\2">\1</a>', caption)
        caption = re.sub(r'<a href="@(.+)">(.+)</a>', r'<a href="https://t.me/\1">\2</a>', caption)

    bot.send_photo(photo, caption=caption, chat_id=to)


class On:
    @staticmethod
    def start():
        return telegram.on.command('start')

    @staticmethod
    def photo():
        return telegram.on.photo()

    @staticmethod
    def text(value: str):
        return telegram.on.text(value)


on = On()
kb = ...
