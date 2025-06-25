from django import forms
from .models import Curso, Interesse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class InteresseForm(forms.ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type':'date'}),
        }

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    