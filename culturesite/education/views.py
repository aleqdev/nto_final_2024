from django.shortcuts import render
from django.http import HttpResponse
from .models import ActInviteStudy
def reportStudy(request):
    context = {"study": {}}
    context["study"]["Студия 1"] = []
    context["study"]["Студия 1"].append({"fio": "Максим", "date": "02.02.2022"})
    return render(request, "education/report_study.html")

