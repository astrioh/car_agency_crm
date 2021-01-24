from django.shortcuts import render

def clients_all_view(request, *args, **kwargs):
    return render(request, "clients/all.html", status=200)

def contracts_all_view(request, *args, **kwargs):
    return render(request, "contracts/all.html", status=200)

def dealers_all_view(request, *args, **kwargs):
    return render(request, "dealers/all.html", status=200)

def employees_all_view(request, *args, **kwargs):
    return render(request, "employees/all.html", status=200)

def cars_all_view(request, *args, **kwargs):
    return render(request, "cars/all.html", status=200)