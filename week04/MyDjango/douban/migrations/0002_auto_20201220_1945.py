# Generated by Django 2.2.13 on 2020-12-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Douban_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
                ('comment', models.CharField(max_length=400)),
                ('comment_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='File_comment',
        ),
    ]
