# Generated by Django 5.0.4 on 2024-04-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_siteuser_follows_alter_siteuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='djangodbmodelsquery_utilsdeferredattribute-object-at-0x000002b775442c30', max_length=100),
        ),
    ]
