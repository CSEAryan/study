# Generated by Django 4.2.18 on 2025-03-06 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_student_remove_video_duration_remove_video_max_grade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
    ]
