# Generated by Django 2.2.12 on 2020-04-27 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0015_auto_20200427_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settinguser',
            name='Site',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='wiki.Sites'),
        ),
    ]
