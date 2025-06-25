from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Interesse
from .forms import CursoForm, InteresseForm, CadastroUsuarioForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login


# Create your views here.

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render (request, 'cursos/lista_cursos.html', {'cursos': cursos})

@login_required
@permission_required('cursos.add_curso', raise_exception=True)
def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm
    return render(request, 'cursos/cadastrar_curso.html', {'form':form})


@login_required
@permission_required('cursos.change_curso', raise_exception=True)
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request,'cursos/editar_curso.html', {'form':form, 'curso':curso})

@login_required
@permission_required('cursos.delete_curso', raise_exception=True)
def excluir_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'cursos/excluir_curso.html', {'curso':curso})


@login_required
def lista_interesses(request):
    interesses = Interesse.objects.all()
    return render(request, 'cursos/lista_interesses.html',{'interesses':interesses})

def cadastrar_interesse(request):
    if request.method == 'POST':
        form = InteresseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cursos/sucesso_interesse.html')
    else:
        form = InteresseForm()
    return render(request, 'cursos/cadastrar_interesse.html', {'form':form})

@login_required
def detalhe_interesse(request, interesse_id):
    interesse = get_object_or_404(Interesse, id=interesse_id)
    return render(request, 'cursos/detalhe_interesse.html', {'interesse':interesse})

@login_required
def index(request):
    return render(request, 'cursos/index.html')


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cursos/cadastro_usuario.html', {'form':form})


    


