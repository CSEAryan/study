# Generated by Django 4.2.18 on 2025-03-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentprofile_delete_student_remove_video_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.URLField(default='https://www.youtube.com/embed/NybHckSEQBI'),
        ),
    ]
