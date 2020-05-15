# Generated by Django 3.0.5 on 2020-05-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200419_0051'),
        ('cart', '0008_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Products'),
        ),
    ]