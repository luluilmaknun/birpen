# Generated by Django 3.0.3 on 2020-02-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengumuman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengumuman',
            name='komentar',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
