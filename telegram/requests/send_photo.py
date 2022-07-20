from .base import ReplyMarkupT
from ..api import request
from ..context import ctx
from ..objects import Translations, MessageEntity, Message, InputFile
from ..objects.tg_methods import SendPhoto


def send_photo(
        photo: InputFile | str,
        caption: str | Translations = None,
        reply_markup: ReplyMarkupT = None,

        chat_id: int | str = None,
        parse_mode: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,

        reply_to_message_id: int = None,
        caption_entities: list[MessageEntity] = None,
        allow_sending_without_reply: bool = None,
) -> Message:
    return request(
        SendPhoto,
        locals(),
        chat_id=ctx.chat_id,
        parse_mode=ctx.parse_mode,
        disable_notification=ctx.disable_notification,
        protect_content=ctx.protect_content,
    )
