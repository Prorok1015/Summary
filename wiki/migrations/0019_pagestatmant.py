# Generated by Django 3.0.5 on 2020-04-29 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0018_auto_20200427_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageStatmant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Page')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
