from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from . import forms as dashboard_forms
from .models import Student
# from wkhtmltopdf.views import PDFTemplateResponse
from django.template.loader import get_template
from django.views.generic import View
from .models import Class
from django.db.models import Q
import io
from django.http import FileResponse


# from reportlab.pdfgen import canvas


def index(request):
    obj = Student.objects.all()
    return render(request, "dashboard/index.html", {"obj": obj})


@csrf_exempt
def detail(request, id=None):
    obj = get_object_or_404(Student, pk=id)
    year_form = dashboard_forms.YearForm(request.POST or None)
    if request.method == 'POST':
        classes = obj.classes.all().filter(year__year=str(request.POST.get('year')))
    else:
        classes = obj.classes.all()
    context = {'object': obj, 'classes': classes, "form": year_form}
    return render(request, 'dashboard/detail.html', context)


def grades_pdf(request):
    pass
    # # Retrieve the selected grades data from the request
    # selected_grades = request.POST.getlist('selected_grades')
    #
    #
    # # Create a PDF file in memory
    # buffer = io.BytesIO()
    # p = canvas.Canvas(buffer)
    #
    # # Write the selected grades to the PDF
    # for grade in selected_grades:
    #     p.drawString(100, 100, grade)
    #
    # # Close the PDF file
    # p.showPage()
    # p.save()
    #
    # # Get the value of the BytesIO buffer and create a FileResponse
    # pdf = buffer.getvalue()
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="grades.pdf"'
    #
    # return response


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            error_message = "Username or Password is incorrect!"
            return render(request, "home/login.html", {"error_message": error_message})

    return render(request, "home/login.html")


def logout(request):
    return redirect("login")


def dashboard(request):
    return redirect("login")
