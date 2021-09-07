from django.urls import path

from courses.views import hello_django, speciality, teacher, subject, sub_detail, speciality_create, teacher_create, \
    subject_create

urlpatterns = [
    path('', hello_django, name="hello-django"),
    path('speciality/', speciality, name='speciality'),
    path('teacher/', teacher, name='teachers'),
    path('subject/', subject, name='subject'),
    path('subject/<int:pk>/', sub_detail, name='sub_detail'),
    path('speciality/create', speciality_create, name='speciality_create'),
    path('teacher/create', teacher_create, name='teacher_create'),
    path('subject/create', subject_create, name='subject_create')
]
