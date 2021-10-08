# Generated by Django 3.2.6 on 2021-10-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("giftcard", "0010_auto_20211007_0547"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="giftcard",
            name="giftcard_p_meta_idx",
        ),
        migrations.RemoveIndex(
            model_name="giftcard",
            name="giftcard_meta_idx",
        ),
        migrations.RemoveIndex(
            model_name="giftcard",
            name="giftcard_search_gin",
        ),
        migrations.RemoveField(
            model_name="giftcard",
            name="tag",
        ),
        migrations.AlterField(
            model_name="giftcardevent",
            name="type",
            field=models.CharField(
                choices=[
                    ("issued", "The gift card was created be staff user or app."),
                    ("bought", "The gift card was bought by customer."),
                    ("updated", "The gift card was updated."),
                    ("activated", "The gift card was activated."),
                    ("deactivated", "The gift card was deactivated."),
                    ("balance_reset", "The gift card balance was reset."),
                    ("expiry_date_updated", "The gift card expiry date was updated."),
                    ("tags_updated", "The gift card tags were updated."),
                    ("sent_to_customer", "The gift card was sent to the customer."),
                    ("resent", "The gift card was resent to the customer."),
                    ("note_added", "A note was added to the gift card."),
                    ("used_in_order", "The gift card was used in order."),
                ],
                max_length=255,
            ),
        ),
    ]
