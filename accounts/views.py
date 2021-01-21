from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


from .forms import SignUpForm, LoginForm
from employees.models import Employee, Role


def login_view(request, *args, **kwargs):
    form = LoginForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/cars/")

    context = {
        "form": form,
        "btn_label": "Войти",
        "title": "Войти"
    }

    return render(request, "auth/auth.html", context)


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/")

    context = {
        "form": None,
        "btn_label": "Выйти",
        "title": "Выход",
        "description": "Вы точно хотите выйти?",
    }

    return render(request, "auth/auth.html", context)


def register_view(request, *args, **kwargs):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=True)
        user.refresh_from_db()
        user.set_password(form.cleaned_data.get("password1"))

        user.save()

        last_name = form.cleaned_data.get("last_name")
        first_name = form.cleaned_data.get("first_name")
        middle_name = form.cleaned_data.get("middle_name")
        sex = form.cleaned_data.get("sex")
        birthday = form.cleaned_data.get("birthday")
        pass_series = form.cleaned_data.get("pass_series")
        pass_number = form.cleaned_data.get("pass_number")
        inn = form.cleaned_data.get("inn")
        email = form.cleaned_data.get("email")
        address = form.cleaned_data.get("address")
        phone = form.cleaned_data.get("phone")
        
        role = form.cleaned_data.get("role")

        employee = Employee(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            sex=sex,
            birthday=birthday,
            pass_series=pass_series,
            pass_number=pass_number,
            inn=inn,
            email=email,
            address=address,
            phone=phone,
            role=role,
            user=user
        )

        employee.save()

        login(request, user)

        return redirect("/")

    context = {
        "form": form,
        "btn_label": "Зарегистрироваться",
        "title": "Регистрация"
    }

    return render(request, "auth/auth.html", context)
