from django.http import HttpResponse
from django.shortcuts import render, redirect

from courses.forms import SpecialityForm, TeacherForm, SubjectForm
from courses.models import Speciality, Teacher, Subject

def subject_create(request):
    if request.method == 'GET':
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subject")

    return render(request, "courses/subject_create.html", {
        "form": form,
    })

def teacher_create(request):
    if request.method == 'GET':
        form = TeacherForm()
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teachers")

    return render(request, "courses/teacher_create.html", {
        "form": form,
    })

def speciality_create(request):
    if request.method == 'GET':
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            spec = Speciality.objects.create(
                name=data['name'],
                code=data['code'],
            )
            return redirect("speciality")


    return render(request, "courses/speciality_create.html", {
        "form": form,
    })

def sub_detail(request, pk):
    subject = Subject.objects.get(pk=pk)

    return render(request, "courses/sub_detail.html", {
        "subject": subject
    })

def subject(request):
    subjects = Subject.objects.all()
    return render(request, "courses/subject.html",{
        "subjects": subjects,
    })

def teacher(request):
    name = request.GET.get('search')
    if not name:
        teachers = Teacher.objects.all()
    else:
        teachers = Teacher.objects.filter(first_name__contains=name)

    return render(request, 'courses/teacher.html', {
        'teachers': teachers
    })


def speciality(request):
    special = Speciality.objects.all()
    return render(request, "courses/speciality.html",{
        "special": special,
    })

def hello_django(request):
    name = request.GET.get('name', 'Django')
    return HttpResponse(f"Hello {name}")

