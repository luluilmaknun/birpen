# Generated by Django 3.0.4 on 2020-05-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sso_ui', '0008_auto_20200420_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='year_of_entry',
            field=models.CharField(blank=True, max_length=4, verbose_name='Tahun masuk'),
        ),
    ]
