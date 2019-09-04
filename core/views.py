from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def form1(request):
    return render(request, 'ajax_forms/form1.html')


def form2(request):
    return render(request, 'ajax_forms/form2.html')
