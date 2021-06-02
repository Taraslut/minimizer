from django.db import models


class Link(models.Model):
    main_link = models.CharField(max_length=300, verbose_name="URL", db_index='url_link_index')
    base_link = models.CharField(main_link=300, blank=True)
    redirects = models.IntegerField(verbose_name="Number of redirects")
    min_url_link = models.CharField(max_length=100, verbose_name="Shorten URL")

