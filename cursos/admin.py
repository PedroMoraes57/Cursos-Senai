from django.contrib import admin
from .models import Curso, Interesse


# Dica: Use o método adequado do admin para tomar o modelo 'Curso' visível e gerenciável no admin do Django

admin.site.register(Curso)
admin.site.register(Interesse)

