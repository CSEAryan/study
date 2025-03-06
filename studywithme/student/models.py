from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    GRADE_CHOICES = [
        ("6", "Grade 6"),
        ("7", "Grade 7"),
        ("8", "Grade 8"),
        ("9", "Grade 9"),
        ("10", "Grade 10"),
    ]
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.name} - Grade {self.grade}"

    def get_grade_display_name(self):
        return dict(self.GRADE_CHOICES)[self.grade]


class Video(models.Model):

    GRADE_CHOICES = Student.GRADE_CHOICES

    title = models.CharField(max_length=200)
    description = models.TextField(default="No description provided.")
    url = models.URLField(default="https://example.com/placeholder-video")
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default="1")

    def __str__(self):
        return f"{self.title} - Grade {self.grade}"
