import re

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import PrimaryClass, Staff, Student, Subject


class ClassForm(ModelForm):

    class Meta:
        model = PrimaryClass
        fields = ['class_name']


class SubjectForm(ModelForm):

    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_mark']

        # def clean_subject_mark(self):
        #     mark = self.cleaned_data['subject_mark']
        #     if not re.match(r'^[0-9]*$', mark):
        #         raise forms.ValidationError("Pls Numbers")

        # def clean(self):
        #     cd = self.cleaned_data
        #     validate_integer(cd.get('subject_mark', None))


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['student_name', 'gender']

    def clean_student_name(self):
        name = self.cleaned_data['student_name']
        if not re.match(r'^[a-zA-Z ]+$', name):
            raise ValidationError(_('Field should not have special characters'))
        return name


class StaffForm(ModelForm):

    class Meta:
        model = Staff
        fields = ['staff_name', 'gender']


def validate_mark(value):
    if value == 'N/A':
        pass
    elif int(value) < 0 or int(value) > 100:
        raise ValidationError(_('%(value)s is only between 0 to 100'), params={'value': value},)
    elif not re.match(r'^[0-9]+$', value):
        raise ValidationError(_('No Characters allowed here'))


class StudentMarkForm(forms.Form):
    Tamil = forms.CharField(max_length=3, validators=[validate_mark])
    English = forms.CharField(max_length=3, validators=[validate_mark])
    Maths = forms.CharField(max_length=3, validators=[validate_mark])
    Science = forms.CharField(max_length=3, validators=[validate_mark])
    Social = forms.CharField(max_length=3, validators=[validate_mark])


# def validate_StudentGeneratorbox(value):
#     if re.match(r'^[0-9]$'):
#         raise ValidationError(_('%(value)s% is not allowed'))


class StudentGeneratorbox(forms.Form):
    STUDENT_NAME = forms.CharField(widget=forms.Textarea, required=True)


def validate_period(value):
    if not re.match(r'^[\d+]+$', value):
        raise ValidationError(_('%(value)s is not allowed'), params={'value': value},)


class Table(forms.Form):
    subject_period_1 = forms.CharField(max_length=10, validators=[validate_period])
    subject_period_2 = forms.CharField(max_length=10, validators=[validate_period])
    subject_period_3 = forms.CharField(max_length=10, validators=[validate_period])
    subject_period_4 = forms.CharField(max_length=10, validators=[validate_period])
    subject_period_5 = forms.CharField(max_length=10, validators=[validate_period])
    subject_period_6 = forms.CharField(max_length=10, validators=[validate_period])
