from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('cursos/', views.listar_cursos, name='lista_cursos'),
    path('cursos/novo/', views.cadastrar_curso, name='cadastrar_curso'),
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('cursos/excluir/<int:curso_id>/', views.excluir_curso, name='excluir_curso'),
    path('', views.index, name='index'),
    path('interesses/', views.lista_interesses, name='lista_interesses'),
    path('interesses/novo/', views.cadastrar_interesse, name='cadastrar_interesse'),
    path('interesses/<int:interesse_id>/', views.detalhe_interesse, name='detalhe_interesse'),
    path('login/', LoginView.as_view(template_name='cursos/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='cursos/logout.html'), name='logout'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro_usuario'),
]