from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    class UserType(models.TextChoices):
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 기본 유저 모델
    nickname = models.CharField(max_length=30)  # 닉네임
    bookmarks = models.ManyToManyField('tour_theme.TourTheme', blank=True)  # 북마크한 테마 (선배용)
    likes = models.ManyToManyField('tour_theme.Tour', blank=True)  # 좋아요한 투어 (후배용)
    follows = models.ManyToManyField('self', symmetrical=False, related_name='follower', blank=True)  # 내가 팔로우하는 유저
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follow', blank=True)  # 나를 팔로우하는 유저
    user_type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.JUNIOR
    )  # 유저 타입 (선배, 후배)
    reputation = models.PositiveIntegerField(default=0)  # 평판 점수
