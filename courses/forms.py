from django import forms
from django.forms import ModelForm
from courses.models import Teacher, Subject



class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'



class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.IntegerField(min_value=1)
