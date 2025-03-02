from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)

    class Meta:
        unique_together = ("name", "grade")

    def __str__(self):
        return f"{self.name} (Grade: {self.grade})"


class Video(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)
    video_file = models.FileField(upload_to="videos/")

    def __str__(self):
        return f"{self.title} (Grade: {self.grade})"
