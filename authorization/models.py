from django.db import models


class Article(models.Model):
    poster = models.ImageField(verbose_name='Баннер', upload_to='images/', default='')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст статьи')
    next_article = models.URLField(verbose_name="Следующая статья", default="#")
    prev_article = models.URLField(verbose_name="Предыдущая статья", default="#")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')
    author = models.CharField(max_length=256, verbose_name='Автор')

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return f"/articles/{self.id}"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
