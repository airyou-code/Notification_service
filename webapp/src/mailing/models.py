from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
import pytz


class Mailing(models.Model):
    clients = models.JSONField("Filter for Client List", null=False)
    start_time = models.DateTimeField("Start Time", auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField("End Time", auto_now=False, auto_now_add=False, null=True, blank=True)
    text = models.CharField("Message Text", max_length=250)

    def __str__(self):
        return f"Mailing {self.pk} start {self.start_time}"


class Client(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?7?\d{11}$",
        message="Phone number in 7XXXXXXXXXX format (X is a digit from 0 to 9), Up to 11 digits not allowed"
    )

    phone_number = models.CharField( "Phone number",validators=[phone_regex], max_length=11,blank=True)
    operator = models.IntegerField("Operator code",validators=[MaxValueValidator(999), MinValueValidator(900)])
    tag = models.CharField("Tag", max_length=50)
    timezone = models.CharField(max_length=32, choices=tuple(zip(pytz.all_timezones, pytz.all_timezones)), default="UTC")


class Message(models.Model):
    client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.CASCADE)
    mailing = models.ForeignKey(Mailing, verbose_name="Mailing", on_delete=models.CASCADE)
    sending_status = models.BooleanField("Status", default=False)
    start_date = models.DateTimeField(verbose_name="Start time", auto_now=True)

    def __str__(self):
        return f"Message id {self.pk} in mobile {self.client.phone_number} "


