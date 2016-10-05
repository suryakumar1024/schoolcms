from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import context
from django.conf import settings
from form import ClassForm, StaffForm, StudentForm, SubjectForm, StudentMarkForm
from models import PrimaryClass, Subject, Staff, Student
import collections
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    if PrimaryClass.objects.exists():
        instance_class = PrimaryClass.objects.all()
        return render(request, 'school/index.html', {'classes': instance_class})
    else:
        for standards in settings.PRIMARY_CLASSES:
            instance_primary_class = PrimaryClass.objects.create(class_name=standards)
            for subjects in settings.SUBJECTS:
                Subject.objects.create(fk_primary_class=instance_primary_class, subject_name=subjects)

        for i, standard in enumerate(settings.PRIMARY_CLASSES):
            instance_primary_class = PrimaryClass.objects.get(class_name=standard)
            instance_sub = Subject.objects.get(fk_primary_class=instance_primary_class, subject_name=settings.SUBJECTS[i])

            Staff.objects.create(fk_primary_class=instance_primary_class,fk_subject=instance_sub,staff_name=settings.STAFF[i],
                                 gender='M')
    return render(request, 'school/index.html')


def get_time_table(no_of_staff, no_of_classes):
    container_dict = collections.OrderedDict()
    cls_dict = collections.OrderedDict()
    for contain in range(no_of_classes):
        container_dict['class' + str(contain + 1)] = collections.OrderedDict()
        container_dict['staff' + str(contain + 1)] = collections.OrderedDict()
        for i in range(1, 6):
            p = 0
            staffs = range(1, no_of_staff)
            for j in range(1, 7):
                c = j + contain
                if c > no_of_staff:
                    p = c - no_of_staff
                    container_dict['class' + str(contain + 1)][(i, j)] = p
                    container_dict['staff' + str(contain + 1)][(i, j)] = p
                else:
                    container_dict['class' + str(contain + 1)][(i, j)] = c
                    container_dict['staff' + str(contain + 1)][(i, j)] = c
    return container_dict


def add_student(request, cls):
    if request.method == 'GET':
            form = StudentForm()
            return render(request, 'school/add_student.html', {'form': form, 'cls': cls})
    else:
        form = StudentForm(request.POST)
        class_instance = get_object_or_404(PrimaryClass,pk=cls)
        if form.is_valid():
            add_std_inst = form.save(commit=False)
            add_std_inst.fk_primary_class = class_instance
            add_std_inst.save()
            for sub in settings.SUBJECTS:
                Subject.objects.create(fk_primary_class=class_instance, fk_student=add_std_inst, subject_name =sub)

            return HttpResponseRedirect(reverse('index'))
    return render(request, 'school/index.html')


def get_class_details(request, cls):
    cls_inst = get_object_or_404(PrimaryClass, pk=cls)
    student_instance = Student.objects.filter(fk_primary_class=cls_inst)
    class_instance = get_object_or_404(PrimaryClass, pk=cls)
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']

    if class_instance.class_name == 'FIRST STANDARD':
        class_timetable = get_time_table(5, 5)['class1']
    elif class_instance.class_name == 'SECOND STANDARD':
        class_timetable = get_time_table(5, 5)['class2']
    elif class_instance.class_name == 'THIRD STANDARD':
        class_timetable = get_time_table(5, 5)['class3']
    elif class_instance.class_name == 'FOURTH STANDARD':
        class_timetable = get_time_table(5, 5)['class4']
    elif class_instance.class_name == 'FIFTH STANDARD':
        class_timetable = get_time_table(5, 5)['class5']

    return render(request, 'school/timetable.html', {'class_timetable': class_timetable,
                                                     'days': days, 'class_instance': class_instance,
                                                     'student_instance': student_instance})


def addmark(request, std):
    if request.method == 'GET':
        form = StudentMarkForm()
    else:
        import ipdb; ipdb.set_trace()
        form = StudentMarkForm(request.POST)
        if form.is_valid():
            tamil_mark = form.cleaned_data['Tamil']
            english_mark = form.cleaned_data['English']
            maths_mark = form.cleaned_data['Maths']
            science_mark = form.cleaned_data['Science']
            social_mark = form.cleaned_data['Social']

            # std_ins = get_object_or_404(Student, id=std)
            subject_qs = Subject.objects.filter(fk_student_id=std)

            tam_sub = subject_qs.get(subject_name='TAMIL')
            tam_sub.subject_mark = tamil_mark
            tam_sub.save()

            eng_sub = subject_qs.get(subject_name='ENGLISH')
            eng_sub.subject_mark = english_mark
            eng_sub.save()

            mat_sub = subject_qs.get(subject_name='MATHS')
            mat_sub.subject_mark = maths_mark
            mat_sub.save()

            sci_sub = subject_qs.get(subject_name='SCIENCE')
            sci_sub.subject_mark = science_mark
            sci_sub.save()

            soc_sub = subject_qs.get(subject_name='SOCIAL')
            soc_sub.subject_mark = social_mark
            soc_sub.save()

            return HttpResponseRedirect(reverse('index'))
    return render(request, 'school/add_mark.html', {'form': form, 'std': std})

