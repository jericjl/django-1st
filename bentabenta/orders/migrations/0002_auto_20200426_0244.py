# Generated by Django 3.0.5 on 2020-04-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=65),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=120),
        ),
    ]