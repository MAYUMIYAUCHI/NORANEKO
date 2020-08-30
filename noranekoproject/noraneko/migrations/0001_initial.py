# Generated by Django 2.2.15 on 2020-08-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NekoPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=255, verbose_name='名前')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
