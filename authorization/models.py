from django.db import models


class Article:
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=256)

    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return self.title
