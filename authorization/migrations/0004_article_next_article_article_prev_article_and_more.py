# Generated by Django 4.1.1 on 2022-09-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_auto_20211130_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='next_article',
            field=models.URLField(default='#', verbose_name='Следующая статья'),
        ),
        migrations.AddField(
            model_name='article',
            name='prev_article',
            field=models.URLField(default='#', verbose_name='Предыдущая статья'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
