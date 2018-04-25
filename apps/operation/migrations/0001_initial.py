# Generated by Django 2.0.3 on 2018-04-19 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonAskAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=500, verbose_name='回复内容')),
                ('reply_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='回复时间')),
            ],
            options={
                'verbose_name': '问题回复',
                'verbose_name_plural': '问题回复',
            },
        ),
        migrations.CreateModel(
            name='LessonUserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='问题内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='提问时间')),
            ],
            options={
                'verbose_name': '课程提问',
                'verbose_name_plural': '课程提问',
            },
        ),
        migrations.CreateModel(
            name='LessonUserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '课程评论',
                'verbose_name_plural': '课程评论',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户课程',
                'verbose_name_plural': '用户课程',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(verbose_name='被收藏的id')),
                ('fav_type', models.IntegerField(choices=[(1, 'course'), (2, 'teacher'), (3, 'org')], verbose_name='收藏类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='接收用户')),
                ('message', models.CharField(max_length=500, verbose_name='消息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
    ]