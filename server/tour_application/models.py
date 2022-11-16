from django.db import models


class TourApplication(models.Model):

    tour = models.OneToOneField(
        "tour.Tour",
        related_name="tour_application",
        on_delete=models.CASCADE,
        verbose_name="투어"
    )

    user = models.ManyToManyField(
        "user.Profile",
        related_name="tour_application",
        verbose_name="투어참가유저"
    )

    participants_on_site = models.IntegerField(default=0, blank=True)

    tour_finished = models.BooleanField(default=False, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="참가신청일시")

    class Meta:
        db_table = "tour_application"
        verbose_name = "투어신청서"
        verbose_name_plural = "투어신청서"