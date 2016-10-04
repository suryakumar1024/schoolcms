from django.shortcuts import render
import collections
# Create your views here.


def index(request):
    return render(request, 'schooltimetable/index.html', {'table': get_time_table(5,5)})


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
