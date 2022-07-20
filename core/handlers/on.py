from telegram import handlers


class On:

    @staticmethod
    def start(callback):
        return handlers.command('start')(callback)

    @staticmethod
    def photo(callback):
        return handlers.photo()(callback)

    @staticmethod
    def text(callback):
        return handlers.text()(callback)

    def __call__(self, text: str):
        def deco(callback):
            return handlers.text(text)(callback)

        return deco


on = On()
