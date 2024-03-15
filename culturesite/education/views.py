from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def reportStudy(request):
    st = Study.objects.all()
    a = ActInviteStudy.objects.all()
    context = {"study": {}, "test": "test"}
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



def reportAboniment(request):
    context = {"study": {}}
    st = AbonementBuy.objects.all()
    study = Study.objects.all()
    price_abonement = AbonementPriceSet.objects.all()
    all_price = 0
    for obj in study:
        if (context["study"].get(obj.name) is None):
            context["study"][obj.name] = {"priceSingle": 0, "cntSingle": 0, "priceMonth": 0, "cntMonth": 0, "priceYear": 0, "cntYear": 0, "allPriceSingle": 0, "allPriceMonth": 0, "allPriceYear": 0, "allPrice": 0}
    for obj in price_abonement:
        context["study"][obj.act_study_start_order.study.name]["priceSingle"] = obj.price_single
        context["study"][obj.act_study_start_order.study.name]["priceMonth"] = obj.price_month
        context["study"][obj.act_study_start_order.study.name]["priceYear"] = obj.price_year
    for obj in st:
        if (obj.type_abonement == "разовый"):
            context["study"][obj.start_order_study.study.name]["cntSingle"] += 1
            context["study"][obj.start_order_study.study.name]["allPriceSingle"] += obj.price
        if (obj.type_abonement == "месячный"):
            context["study"][obj.start_order_study.study.name]["cntMonth"] += 1
            context["study"][obj.start_order_study.study.name]["allPriceMonth"] += obj.price
        if (obj.type_abonement == "годовой"):
            context["study"][obj.start_order_study.study.name]["cntYear"] += 1
            context["study"][obj.start_order_study.study.name]["allPriceYear"] += obj.price
        context["study"][obj.start_order_study.study.name]["allPrice"] += obj.price
        all_price += obj.price
    context["all_price"] = all_price
    return render(request, "education/report_aboniment.html", context)