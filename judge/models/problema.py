from django.db import models
from judge.models.categoria import Categoria
from judge.models.teste import Teste
from judge.models.base_model import BaseModel
from django.core.validators import MinLengthValidator
from judge.enums.nota import Nota
from judge.enums.limite_memoria import LimiteMemoria
from judge.enums.limite_tempo import LimiteTempo
from judge.enums.idioma import Idioma
from judge.enums.dificuldade import Dificuldade
from datetime import datetime



class Problema(BaseModel):

    cod = models.CharField(
        validators=[MinLengthValidator(4)],
        max_length=20, 
        unique=True
    )

    titulo = models.CharField(
        validators=[MinLengthValidator(5)],
        max_length=200
    )

    enunciado = models.TextField(
        validators=[MinLengthValidator(10)],
        max_length=5000
    )

    enunciado_entrada = models.TextField(
        validators=[MinLengthValidator(10)],
        max_length=2000
    )

    enunciado_saida = models.TextField(
        validators=[MinLengthValidator(10)],
        max_length=2000
    )

    dificuldade = models.CharField(
        choices=Dificuldade.choices
    )

    idioma = models.CharField(
        choices=Idioma.choices
    )

    fonte = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=150
    )

    limite_tempo_ms = models.CharField(
        choices=LimiteTempo.choices,
        default=LimiteTempo.S1
    )

    limite_memoria_mb = models.CharField(
        choices=LimiteMemoria.choices,
        default=LimiteMemoria.MB32
    )

    publico = models.BooleanField(
        default=True
    )


    nota = models.IntegerField(
        choices = Nota.choices
    )


    criado = models.DateTimeField(
        default = datetime.now()
    )
    
    atualizado = models.DateTimeField(
        default = datetime.now()
    )

    categorias = models.ManyToManyField(Categoria)

    testes = models.ManyToManyField(Teste)



    def __str__(self):
        return f"{self.cod} - {self.titulo}"