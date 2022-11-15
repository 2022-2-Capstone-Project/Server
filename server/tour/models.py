from django.db import models

from user.models import Profile
from tour_theme.models import TourTheme


class Tour(models.Model):
    tourName = models.CharField(max_length=256, verbose_name="투어이름")
    date = models.CharField(max_length=50, verbose_name="투어일시")
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    thumbnail = models.URLField(verbose_name="썸네일")
    description = models.TextField(verbose_name="투어설명")
    participants = models.PositiveIntegerField(verbose_name="정원")  # 설정 참여자 수
    start_place = models.CharField(max_length=100, verbose_name="시작장소")  # 시작 장소
    latitude = models.FloatField(verbose_name="시작장소 위도")  # 위도
    longitude = models.FloatField(verbose_name="시작장소 경도")  # 경도
    profile_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        db_column="profile_id",
        verbose_name="생성유저"
    )
    theme_id = models.ForeignKey(
        TourTheme,
        on_delete=models.CASCADE,
        db_column="theme_id",
        verbose_name="테마이름"
    )

    class Meta:
        db_table = "tour"
        verbose_name = "투어"
        verbose_name_plural = "투어"
