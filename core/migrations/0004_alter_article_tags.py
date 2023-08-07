# Generated by Django 4.2.1 on 2023-06-16 10:06

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('core', '0003_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='Use comma to separate tags, # is not needed to add tag', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
