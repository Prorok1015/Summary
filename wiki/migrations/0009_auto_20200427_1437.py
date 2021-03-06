# Generated by Django 2.2.12 on 2020-04-27 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_auto_20200426_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settinguser',
            name='Site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wiki.Sites'),
        ),
        migrations.AlterField(
            model_name='settinguser',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='settinguser',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wiki.Categorys'),
        ),
    ]
