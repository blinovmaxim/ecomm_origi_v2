# Generated by Django 4.1.1 on 2022-10-30 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_remove_order_email_order_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.deliveryaddress",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.city",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.country",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.region",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone_number",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="order",
            name="post_office_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="orders.order",
            ),
        ),
    ]
