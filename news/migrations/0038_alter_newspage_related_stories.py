# Generated by Django 3.2.13 on 2022-07-02 08:16

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0037_alter_newspage_related_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='related_stories',
            field=wagtail.fields.StreamField([('related_story', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True, use_json_field=None),
        ),
    ]
