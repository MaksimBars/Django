# Generated by Django 2.0.4 on 2018-04-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20180422_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_title',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='Home Title'),
            preserve_default=False,
        ),
    ]
