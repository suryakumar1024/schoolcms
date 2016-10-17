from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

GENDER_CHOICES = (('F', 'Female'), ('M', 'Male'))


class PrimaryClass(models.Model):
    class_name = models.CharField(max_length=128, null=False, blank=False)

    def __unicode__(self):
        return self.class_name


class Student(models.Model):
    fk_primary_class = models.ForeignKey(PrimaryClass)
    student_name = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='-')

    class Meta:
        ordering = ['student_name']

    def __unicode__(self):
        return '%s - %s' %(self.fk_primary_class.class_name, self.student_name)

    def get_total_mark(self):
        total = 0
        subjs = Subject.objects.filter(fk_student=self)
        for each in subjs:
            if each.subject_mark == 'N/A':
                total += 0
            elif each.subject_mark:
                total += int(each.subject_mark)
        return total


class Subject(models.Model):
    fk_primary_class = models.ForeignKey(PrimaryClass)
    fk_student = models.ForeignKey(Student, null=True)
    subject_name = models.CharField(max_length=128, null=False, blank=False)
    subject_mark = models.CharField(max_length=3, null=True, default='N/A')
# validators=[RegexValidator(regex='^[0-9]*$', message='only numbers'),])

    def __unicode__(self):
        return '%s - %s' % (self.fk_primary_class.class_name, self.subject_name)


class Staff(models.Model):
    fk_primary_class = models.OneToOneField(PrimaryClass)
    fk_subject = models.OneToOneField(Subject)
    staff_name = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    def __unicode__(self):
        return '%s - %s' %(self.fk_primary_class.class_name, self.staff_name)


class Timetable(models.Model):
    fk_primary_class = models.ForeignKey(PrimaryClass)
    name_of_day = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name_of_day


class Period(models.Model):
    fk_timetable = models.ForeignKey(Timetable)
    subject_period = models.CharField(max_length=10)

    def __unicode__(self):
        return self.subject_period
