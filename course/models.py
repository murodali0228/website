from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Barchasi(TimeStampedModel):
    ism = models.CharField(null=True, blank=True)
    yozuv = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    intejer = models.IntegerField(null=True, blank=True)
    kichik = models.SmallIntegerField(null=True, blank=True)
    katta = models.BigIntegerField(null=True, blank=True)
    qiziq = models.PositiveIntegerField(null=True, blank=True)
    pozit = models.PositiveSmallIntegerField(null=True, blank=True)
    floa = models.FloatField(null=True, blank=True)
    deci = models.DecimalField(null=True, blank=True)
    sana = models.DateField(null=True, blank=True)
    vaqt = models.TimeField(null=True, blank=True)
    sana_vaqt = models.DateTimeField(null=True, blank=True)
    dura = models.DurationField(null=True, blank=True)
    bol = models.BooleanField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
