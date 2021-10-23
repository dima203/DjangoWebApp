from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_created = models.DateTimeField()
    author = models.CharField(max_length=256)

    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return self.title
