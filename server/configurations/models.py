from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=100)
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    accent_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)
    text_color = models.CharField(max_length=7)
    secondary_text_color = models.CharField(max_length=7)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="Date Published")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")

    def __str__(self):
        return self.name

