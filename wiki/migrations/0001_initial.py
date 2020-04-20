# Generated by Django 2.2.12 on 2020-04-18 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('CategoryName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('SiteName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('summary', models.CharField(max_length=180)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Categorys')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Sites')),
            ],
        ),
    ]
