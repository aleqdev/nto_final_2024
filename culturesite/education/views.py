from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def reportStudy(request):
    st = Study.objects.all()
    a = ActInviteStudy.objects.all()
    context = {"study": {"Студия 1": [{"fio": "Максим", "date": "02.02.2022"}]}, "test": "test"}
    for obj in st:
        if (context["study"].get(obj.name) is None):
            context["study"][obj.name] = []
    for obj in a:
        print(obj.date)
        context["study"][obj.act_study_start_order.study.name].append({"fio": obj.student.fio, "date": str(obj.date)})
    print(context)
    # context["study1"] = []
    # context["study1"].append({"fio": "Максим", "date": "02.02.2022"})
    return render(request, "education/report_study.html", context)

def index(request):
    return render(request, "education/index.html")