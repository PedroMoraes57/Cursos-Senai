from django.db import models
from datetime import date, datetime

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=100) 
    codigo = models.CharField(max_length=10, unique=True) 
    area = models.CharField(max_length=50)
    carga_horaria = models.PositiveIntegerField() 
    modalidade = models.CharField(max_length=50) 
    vagas = models.PositiveIntegerField() 

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Interesse(models.Model):
    nome_interessado = models.CharField(max_length=100) 
    email = models.EmailField() 
    telefone = models.CharField(max_length=20) 
    cidade = models.CharField(max_length=100) 
    data_nascimento = models.DateField() 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    como_conheceu = models.CharField(max_length=50) 
    data_interesse = models.DateTimeField(auto_now_add=True)
    status_contato = models.CharField(max_length=3, choices=[('Sim','Sim'), ('Não', 'Não')], default='Não') 
    observacoes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome_interessado} - {self.curso.nome}"
    @property
    def idade(self):
        from datetime import date
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))