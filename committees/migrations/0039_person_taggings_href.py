# Generated by Django 3.2.10 on 2022-01-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0038_remove_person_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='taggings_href',
            field=models.URLField(null=True),
        ),
    ]
