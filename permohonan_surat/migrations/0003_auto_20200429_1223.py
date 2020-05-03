# Generated by Django 3.0.4 on 2020-04-29 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permohonan_surat', '0002_auto_20200428_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='status_bayar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='permohonan_surat.StatusBayar'),
        ),
        migrations.AlterField(
            model_name='pesanansuratakademik',
            name='status_surat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='permohonan_surat.StatusSurat'),
        ),
    ]
