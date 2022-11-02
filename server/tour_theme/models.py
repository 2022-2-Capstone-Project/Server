from django.db import models
from user.models import Profile


class TourTheme(models.Model):
    title = models.CharField(max_length=100)  # 테마명
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)  # 작성자
    created = models.DateTimeField(auto_created=True, blank=True, null=True)  # 생성일
    estimated = models.IntegerField()  # 예상 소요 시간 (minutes)
    participants = models.PositiveIntegerField()  # 권장 참여자 수
    start_place = models.CharField(max_length=100)  # 시작 장소
    latitude = models.FloatField()  # 위도
    longitude = models.FloatField()  # 경도
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)  # 썸네일


class Tour(models.Model):
    pass