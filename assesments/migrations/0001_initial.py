# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-21 09:05
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('opted_choice', models.TextField(max_length=250)),
                ('written_answer', models.TextField()),
                ('alloted_marks', models.FloatField(max_length=250)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_answer_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_answer_deleted_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('header', models.CharField(max_length=150)),
                ('brief', models.TextField()),
                ('exam_start_date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('exam_start_type', models.CharField(choices=[('auto', 'Automatic'), ('manual', 'Manually')], default='auto', max_length=14)),
                ('passing_marks', models.IntegerField(default=0)),
                ('privilege', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=14)),
                ('is_exam_active', models.BooleanField(default=True)),
                ('expired_on', models.DateTimeField(default=datetime.datetime.now)),
                ('type', models.CharField(default='assessment', editable=False, max_length=10)),
                ('duration_hours', models.IntegerField(null=True)),
                ('duration_minutes', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_assesment_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_assesment_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('subscriber_users', models.ManyToManyField(to='students.Student')),
                ('updated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_assesment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('question_text', models.TextField()),
                ('question_image', models.BinaryField(blank=True, null=True)),
                ('option_one', models.TextField(blank=True, max_length=250, null=True)),
                ('option_two', models.TextField(blank=True, max_length=250, null=True)),
                ('option_three', models.TextField(blank=True, max_length=250, null=True)),
                ('option_four', models.TextField(blank=True, max_length=250, null=True)),
                ('option_five', models.TextField(blank=True, max_length=250, null=True)),
                ('question_type', models.CharField(choices=[('mcq', 'Multiple Choice'), ('scq', 'Single Choice'), ('sqa', 'Text Answer')], default='scq', max_length=14)),
                ('brief_answer', models.TextField(blank=True, null=True)),
                ('max_marks', models.IntegerField()),
                ('correct_options', models.CharField(blank=True, max_length=150, null=True)),
                ('assesment_linked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assesments.Assesment')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_question_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_question_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_question_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('exam_taken_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_question', models.IntegerField(default=0)),
                ('total_attempted', models.IntegerField(default=0)),
                ('total_marks', models.IntegerField(default=0)),
                ('obtained_marks', models.IntegerField(default=0)),
                ('publish_result', models.BooleanField(default=False)),
                ('result_passed', models.BooleanField(default=False)),
                ('type', models.CharField(default='result', editable=False, max_length=10)),
                ('assesment_submitted', models.BooleanField(default=False)),
                ('assesment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assesments.Assesment')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_result_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_result_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('registered_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('updated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_result_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='for_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assesments.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='for_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assesments.Result'),
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_answer_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
