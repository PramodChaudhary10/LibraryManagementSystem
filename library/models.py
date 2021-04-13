from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    section = models.CharField(max_length=10)


class Book(models.Model):
    catchoice = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ('science', 'Science'),
        ('engineering', 'Engineering'),
        ('IT', 'IT'),
    ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=40)
    category = models.CharField(
        max_length=30, choices=catchoice, default='education')
