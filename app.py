from assets import *


@step('*/')
@on.start
def _():
    send('Отправь мне фотографию')


@step('/a1')
@on.photo
def _():
    save('$photo')
    send('В какой канал отправить?', kb.channels)


@step('a1/')
@on(kb.channels.diunder)
def _():
    send_post(to='@diunder')


@step('a1/')
@on(kb.channels.pikzery)
def _():
    send_post(to='@pikzery', caption='[@милые пикчи](@pikzery)')


@step('a1/a2')
@on(kb.channels.akiet)
def _():
    send('Выбери подпись:', kb.signs)


@step('a2/')
@on(kb.signs.anime_pictures)
def _():
    send_post(to='@akiet', caption='[@аниме пикчи](@akiet)')


@step('a2/')
@on(kb.signs.paired_icons)
def _():
    send_post(to='@akiet', caption='[@парные авы](@akiet)')


@step('a1/')
@on(kb.channels.avy_parnye_avatarki)
def _():
    send_post(to='@avy_parnye_avatarki')


@step('*')
@on.text
def _():
    send('?')
