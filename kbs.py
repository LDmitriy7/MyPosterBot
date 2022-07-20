from telegram.objects import ReplyKeyboardRemove


class Signs:
    anime_pictures = '@аниме пикчи'
    paired_icons = '@парные авы'

    def __iter__(self):
        return ([btn] for btn in [self.anime_pictures, self.paired_icons])


class Channels:
    diunder = '@diunder'
    pikzery = '@pikzery'
    akiet = '@akiet'
    avy_parnye_avatarki = '@avy_parnye_avatarki'

    def __iter__(self):
        return ([btn] for btn in [self.diunder, self.pikzery, self.akiet, self.avy_parnye_avatarki])


channels = Channels()
signs = Signs()
remove = ReplyKeyboardRemove()
