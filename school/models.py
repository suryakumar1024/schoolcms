from django.db import models

# Create your models here.

GENDER_CHOICES = (('F', 'Female'), ('M', 'Male'))


class PrimaryClass(models.Model):
    class_name = models.CharField(max_length=128, null=False, blank=False)

    def __unicode__(self):
        return self.class_name


class Student(models.Model):
    fk_primary_class = models.ForeignKey(PrimaryClass)
    student_name = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    def __unicode__(self):
        return '%s - %s' %(self.fk_primary_class.class_name, self.student_name)


class Subject(models.Model):
    fk_primary_class = models.ForeignKey(PrimaryClass)
    fk_student = models.ForeignKey(Student, null=True)
    subject_name = models.CharField(max_length=128, null=False, blank=False)
    subject_mark = models.CharField(max_length=3, null=True, blank=False)

    def __unicode__(self):
        return '%s - %s' % (self.fk_primary_class.class_name, self.subject_name)


class Staff(models.Model):
    fk_primary_class = models.OneToOneField(PrimaryClass)
    fk_subject = models.OneToOneField(Subject)
    staff_name = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    def __unicode__(self):
        return '%s - %s' %(self.fk_primary_class.class_name, self.staff_name)
