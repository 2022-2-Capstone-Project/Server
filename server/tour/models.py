from django.db import models


# Create your models here.
class Tour(models.Model):
    tourName = models.CharField(max_length=256, verbose_name="투어이름")
    date = models.CharField(max_length=50, verbose_name="투어일시")
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    thumbnail = models.URLField(verbose_name="썸네일")
    description = models.TextField(verbose_name="투어설명")
    # user_id = models.ForeignKey(
    #     "user.User",
    #     # related_name="user",
    #     on_delete=models.CASCADE(),
    #     db_column="user_id",
    #     verbose_name="생성유저"
    # )
    # themeId = models.OneToOneField("Theme", on_delete=models.CASCADE(), verbose_name="테마이름")

    class Meta:
        db_table = "tour"
        verbose_name = "투어"
        verbose_name_plural = "투어"