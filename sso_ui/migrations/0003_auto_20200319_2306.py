# Generated by Django 3.0.4 on 2020-03-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sso_ui', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsistenDosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_asdos',
        ),
    ]
