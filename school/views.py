import collections
import random

from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from form import ClassForm, StaffForm, StudentForm, SubjectForm, StudentMarkForm, StudentGeneratorbox
from models import PrimaryClass, Subject, Staff, Student


# Create your views here.


def sort_qs_with_total_mark(student_qs):
    cls_std_sub = collections.OrderedDict()

    unsorted_students = [e for e in student_qs if e.get_total_mark != 0]
    mark_w_zero = [e for e in student_qs if e.get_total_mark == 0]

    while unsorted_students:
        temp_student = unsorted_students[0]
        for each_student in unsorted_students:
            if each_student.get_total_mark() > temp_student.get_total_mark():
                temp_student = each_student

        subj_qs = temp_student.subject_set.all()
        cls_std_sub[temp_student] = subj_qs
        unsorted_students.remove(temp_student)

    for each_student in mark_w_zero:
        subj_qs = each_student.subject_set.all()
        cls_std_sub[each_student] = subj_qs

    return cls_std_sub


def sort_qs_with_sub_name(student_qs, sub_name):
    cls_std_sub = collections.OrderedDict()

    unsorted_students = list(student_qs)

    while unsorted_students:
        temp_student = unsorted_students[0]
        for each_student in unsorted_students:

            if sub_name == 'TAMIL':
                tem_max_mark = temp_student.subject_set.get(subject_name='TAMIL').subject_mark
                each_max_mark = each_student.subject_set.get(subject_name='TAMIL').subject_mark
                if int(each_max_mark) > int(tem_max_mark):
                    temp_student = each_student

            if sub_name == 'ENGLISH':
                tem_max_mark = temp_student.subject_set.get(subject_name='ENGLISH').subject_mark
                each_max_mark = each_student.subject_set.get(subject_name='ENGLISH').subject_mark
                if int(each_max_mark) > int(tem_max_mark):
                    temp_student = each_student

            if sub_name == 'MATHS':
                tem_max_mark = temp_student.subject_set.get(subject_name='MATHS').subject_mark
                each_max_mark = each_student.subject_set.get(subject_name='MATHS').subject_mark
                if int(each_max_mark) > int(tem_max_mark):
                    temp_student = each_student

            if sub_name == 'SCIENCE':
                tem_max_mark = temp_student.subject_set.get(subject_name='SCIENCE').subject_mark
                each_max_mark = each_student.subject_set.get(subject_name='SCIENCE').subject_mark
                if int(each_max_mark) > int(tem_max_mark):
                    temp_student = each_student

            if sub_name == 'SOCIAL':
                tem_max_mark = temp_student.subject_set.get(subject_name='SOCIAL').subject_mark
                each_max_mark = each_student.subject_set.get(subject_name='SOCIAL').subject_mark
                if int(each_max_mark) > int(tem_max_mark):
                    temp_student = each_student

        subj_qs = temp_student.subject_set.all()
        cls_std_sub[temp_student] = subj_qs
        unsorted_students.remove(temp_student)

    return cls_std_sub


def get_time_table(no_of_staff, no_of_classes):
    container_dict = collections.OrderedDict()
    cls_dict = collections.OrderedDict()
    for contain in range(no_of_classes):
        container_dict['class' + str(contain + 1)] = collections.OrderedDict()
        container_dict['staff' + str(contain + 1)] = collections.OrderedDict()
        for i in range(1, 6):
            # staffs = range(1, no_of_staff)
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
            instance_sub = Subject.objects.get(fk_primary_class=instance_primary_class,
                                               subject_name=settings.SUBJECTS[i])

            Staff.objects.create(fk_primary_class=instance_primary_class, fk_subject=instance_sub,
                                 staff_name=settings.STAFF[i],
                                 gender='M')
    return render(request, 'school/index.html')


def add_student(request, cls):
    if request.method == 'GET':
        form = StudentForm()
        class_name = get_object_or_404(PrimaryClass, pk=cls)
        return render(request, 'school/add_student.html', {'form': form, 'cls': cls, 'class_name': class_name})
    else:
        form = StudentForm(request.POST)
        class_instance = get_object_or_404(PrimaryClass, pk=cls)
        if form.is_valid():
            add_std_inst = form.save(commit=False)
            add_std_inst.fk_primary_class = class_instance
            add_std_inst.save()
            for sub in settings.SUBJECTS:
                Subject.objects.create(fk_primary_class=class_instance, fk_student=add_std_inst, subject_name=sub)
    return HttpResponseRedirect(reverse('details', kwargs={'cls': class_instance.id}))


def get_staff_details(request,stf):
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    class_timetable = get_time_table(5, 5)['class'+str(stf)]
    return render(request, 'school/staff_timetable.html', {'days': days, 'class_timetable': class_timetable})


def get_class_details(request, cls, subject=None):
    individual_class_instance = get_object_or_404(PrimaryClass, pk=cls)
    student_qs = Student.objects.filter(fk_primary_class=individual_class_instance)
    list_class_instance = PrimaryClass.objects.all()
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']

    if subject:
        cls_std_sub = sort_qs_with_sub_name(student_qs, subject)
    else:
        cls_std_sub = sort_qs_with_total_mark(student_qs)

    if individual_class_instance.class_name == 'FIRST STANDARD':
        class_timetable = get_time_table(5, 5)['class1']

    elif individual_class_instance.class_name == 'SECOND STANDARD':
        class_timetable = get_time_table(5, 5)['class2']

    elif individual_class_instance.class_name == 'THIRD STANDARD':
        class_timetable = get_time_table(5, 5)['class3']

    elif individual_class_instance.class_name == 'FOURTH STANDARD':
        class_timetable = get_time_table(5, 5)['class4']

    elif individual_class_instance.class_name == 'FIFTH STANDARD':
        class_timetable = get_time_table(5, 5)['class5']

    return render(request, 'school/report.html', {'class_timetable': class_timetable,
                                                  'days': days, 'individual_class_instance': individual_class_instance,
                                                  'cls_std_sub': cls_std_sub,
                                                  'list_class_instance': list_class_instance,
                                                  })


def addmark(request, std):
    std_name = get_object_or_404(Student, pk=std)
    if request.method == 'GET':
        subject_qs = Subject.objects.filter(fk_student_id=std)
        mark_list = []

        for each_subject in settings.SUBJECTS:
            mark_list.append(subject_qs.get(subject_name=each_subject).subject_mark)

        form = StudentMarkForm(initial={'Tamil': mark_list[0], 'English': mark_list[1], 'Maths': mark_list[2],
                                        'Science': mark_list[3], 'Social': mark_list[4]})

    else:
        form = StudentMarkForm(request.POST)
        if form.is_valid():
            tamil_mark = form.cleaned_data['Tamil']
            english_mark = form.cleaned_data['English']
            maths_mark = form.cleaned_data['Maths']
            science_mark = form.cleaned_data['Science']
            social_mark = form.cleaned_data['Social']

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

            std_obj = get_object_or_404(Student, id=std)
            return HttpResponseRedirect(reverse('details', kwargs={'cls': std_obj.fk_primary_class.id}))

    return render(request, 'school/add_mark.html', {'form': form, 'std': std, 'std_name': std_name})


def subject_wise_sorting(request, cls, subject):
    individual_class = get_object_or_404(PrimaryClass, pk=cls)
    student_qs = Student.objects.filter(fk_primary_class=individual_class)
    cls_std_sub = collections.OrderedDict()
    for each_student in student_qs:
        subj_qs = each_student.subject_set.filter(subject_name=subject)
        cls_std_sub[each_student] = subj_qs
    return render(request, 'school/subject_wise_ranking.html', {'cls_std_sub': cls_std_sub})


def delete(request, std):
    student_object =get_object_or_404(Student, pk=std)
    student_object.delete()
    return HttpResponseRedirect(reverse('index'))


def student_generator(request, cls):
    # import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        form = StudentGeneratorbox()
    else:
        form = StudentGeneratorbox(request.POST)
        if form.is_valid():
            form_student_list = form.cleaned_data['STUDNET_NAME']
            student_data = form_student_list.split(",")
            student_list = []
            for student in range(len(student_data)):
                student_list.append((student_data[student].strip()))

            # student_list is obtained
            individual_class = get_object_or_404(PrimaryClass, pk=cls)

            for each_student in student_list:
                student_instance = Student.objects.create(fk_primary_class=individual_class ,
                                                          student_name=each_student)
                for sub in settings.SUBJECTS:
                    Subject.objects.create(fk_primary_class=individual_class, fk_student=student_instance,
                                           subject_name=sub, subject_mark = random.randint(30,100))
            return get_class_details(request, cls)

    return render(request, 'school/student_detail_entry.html', {'form': form, 'cls': cls})
