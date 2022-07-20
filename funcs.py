from core import *
import kbs as kb


def send_post(to: str, caption: str = None):
    send('&photo', **locals())
    send('Ок', kb.remove)
