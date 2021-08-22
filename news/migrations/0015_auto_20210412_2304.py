# Generated by Django 3.1.8 on 2021-04-13 04:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0014_auto_20210412_2254"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documentpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.core.blocks.StreamBlock(
                            [
                                ("header", wagtail.core.blocks.CharBlock()),
                                ("text", wagtail.core.blocks.RichTextBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("quote", wagtail.core.blocks.BlockQuoteBlock()),
                                (
                                    "subsection",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            ("header", wagtail.core.blocks.CharBlock()),
                                            ("text", wagtail.core.blocks.TextBlock()),
                                            (
                                                "subsubsection",
                                                wagtail.core.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "header",
                                                            wagtail.core.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "text",
                                                            wagtail.core.blocks.TextBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
            ),
        ),
    ]
