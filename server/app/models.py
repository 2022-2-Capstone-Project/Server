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

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 기본 유저 모델
    nickname = models.CharField(max_length=30)  # 닉네임
    bookmarks = models.ManyToManyField('TourTheme')  # 북마크한 테마 (선배용)
    likes = models.ManyToManyField('Tour')  # 좋아요한 투어 (후배용)
    follows = models.ManyToManyField('self', symmetrical=False)  # 내가 팔로우하는 유저
    followers = models.ManyToManyField('self', symmetrical=False)  # 나를 팔로우하는 유저
    user_type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.JUNIOR
    )  # 유저 타입 (선배, 후배)
    reputation = models.PositiveIntegerField()  # 평판 점수


class TourTheme(models.Model):
    title = models.CharField(max_length=100)  # 테마명
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)  # 작성자
    estimated = models.DurationField()  # 예상 소요 시간
    participants = models.PositiveIntegerField()  # 권장 참여자 수
    start_place = models.CharField(max_length=100)  # 시작 장소
    latitude = models.FloatField()  # 위도
    longitude = models.FloatField()  # 경도
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)  # 썸네일

