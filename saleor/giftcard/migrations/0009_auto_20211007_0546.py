# Generated by Django 3.2.6 on 2021-10-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("giftcard", "0008_auto_20210818_0633"),
    ]

    operations = [
        migrations.CreateModel(
            name="GiftCardTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="giftcard",
            name="tags",
            field=models.ManyToManyField(
                related_name="gift_cards", to="giftcard.GiftCardTag"
            ),
        ),
    ]
