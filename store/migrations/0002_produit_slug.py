# Generated by Django 5.0.1 on 2024-01-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
