import re

from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.core.validators import validate_integer
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

        # def clean(self):
        #     name = self.student_name
        #     # if not re.match(r'^[a-zA-Z ]+$', name):
        #     if re.match(r'^([^~+&@!#$%]*)$', name):
        #         raise ValidationError(_('Field should not have special characters'))


class StaffForm(ModelForm):

    class Meta:
        model = Staff
        fields = ['staff_name', 'gender']


# class StudentMarkForm(forms.Form):
#     Tamil = forms.IntegerField(min_value=0, max_value=100)
#     English = forms.IntegerField(min_value=0, max_value=100)
#     Maths = forms.IntegerField(min_value=0, max_value=100)
#     Social = forms.IntegerField(min_value=0, max_value=100)
#     Science = forms.IntegerField(min_value=0, max_value=100)


def validate_mark(value):
    if value == 'N/A':
        pass
    elif int(value) < 0 or int(value) > 100:
        raise ValidationError(_('%(value)s is only between 0 to 100'), params={'value': value},)


class StudentMarkForm(forms.Form):
    Tamil = forms.CharField(max_length=3, validators=[validate_mark])
    English = forms.CharField(max_length=3, validators=[validate_mark])
    Maths = forms.CharField(max_length=3, validators=[validate_mark])
    Science = forms.CharField(max_length=3, validators=[validate_mark])
    Social = forms.CharField(max_length=3, validators=[validate_mark])


class StudentGeneratorbox(forms.Form):
    STUDNET_NAME = forms.CharField(widget= forms.Textarea,required=True)