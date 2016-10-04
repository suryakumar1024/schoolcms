from django.db import models

# Create your models here.

CHOICES = (("M", "male"), ("F", "Female"))


class PrimaryClass(models.Model):
    class_name = models.CharField(max_length=50)


class Student(models.Model):
    fk_primary_class = models.ForeignKey(PrimaryClass)
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField(null=True)
    student_sex = models.CharField(choices=CHOICES, max_length=2)


class Subject(models.Model):
    primary_class = models.ForeignKey(PrimaryClass)
    subject_name = models.CharField(max_length=50)
    subject_mark = models.IntegerField()


class Staff(models.Model):
    staff_subject = models.ManyToManyField(Subject)
    staff_name = models.CharField(max_length=50)
    staff_age = models.IntegerField(null=True)
    staff_sex = models.CharField(choices=CHOICES, max_length=2)
