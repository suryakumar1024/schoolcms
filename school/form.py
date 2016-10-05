from django.forms import ModelForm
from django import forms
from models import PrimaryClass, Staff, Student, Subject


class ClassForm(ModelForm):

    class Meta:
        model = PrimaryClass
        fields = ['class_name']


class SubjectForm(ModelForm):

    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_mark']


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['student_name', 'gender']


class StaffForm(ModelForm):

    class Meta:
        model = Staff
        fields = ['staff_name', 'gender']


class StudentMarkForm(forms.Form):
    Tamil = forms.CharField(max_length=3)
    English = forms.CharField(max_length=3)
    Maths = forms.CharField(max_length=3)
    Science = forms.CharField(max_length=3)
    Social = forms.CharField(max_length=3)