# Generated by Django 4.1.4 on 2022-12-31 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0049_rename_main_copy_newspage_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newspage",
            old_name="main_event",
            new_name="related_event",
        ),
    ]
