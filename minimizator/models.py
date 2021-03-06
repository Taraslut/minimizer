from django.db import models


class Link(models.Model):
    main_link = models.CharField(max_length=256, verbose_name="URL")
    redirects = models.IntegerField(verbose_name="Number of redirects", default=0)
    min_url_link = models.CharField(max_length=100, verbose_name="Shorten URL", unique=True)

    def __str__(self):
        return f'{self.base_link} - {self.min_url_link} => {self.redirects}'

