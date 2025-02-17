# Generated by Django 4.1.4 on 2022-12-13 01:59

from django.db import migrations
import news.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0019_alter_newspage_stories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspage",
            name="stories",
            field=wagtail.fields.StreamField(
                [
                    (
                        "related_story",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(required=False)),
                                ("copy", wagtail.blocks.TextBlock(required=False)),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
