from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# MESSAGE
# PK는 django 기본 제공 foreign key 기능이 좋은것 같아서 그냥 Automatic primary key field로 사용하겠습니다.
# 그리고 다른 relationship 관련 기능도 기본적으로 잘 되어있어서 그대로 사용하겠습니다.


class Profile(models.Model):

    class UserType(models.TextChoices):
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')

    user = models.OneToOneField(User, on_delete=models.CASCADE())
    nickname = models.CharField(max_length=30)
    bookmarks = models.ManyToManyField()  # TODO
    follows = models.ManyToManyField("self", symmetrical=False)
    followers = models.ManyToManyField("self", symmetrical=False)
    user_type = models.CharField() # TODO


# TODO
class TourTheme(models.Model):
    pass
