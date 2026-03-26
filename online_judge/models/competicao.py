from django.db import models
from online_judge.models.base_model import BaseModel
from online_judge.models.submissao import Submissao
from django.core.validators import MinValueValidator
#from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from datetime import datetime



class Competicao(BaseModel):

    nome = models.CharField(
        validators=[MinLengthValidator(5)],
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        validators=[MinLengthValidator(3)],
        max_length=50
    )

    descricao = models.TextField(
        validators=[MinLengthValidator(5)],
        max_length=1000
    )

    url = models.URLField(
        null=True
    )

    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    freeze = models.DateTimeField()

    publico = models.BooleanField(
        default=True
    )

    criado = models.DateTimeField(
        default=datetime.now()
    )

    atualizado = models.DateTimeField(
        default=datetime.now()
    )

    penalidade = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    submissao_competicao = models.ForeignKey(
        Submissao,
        on_delete=models.CASCADE,
        null=True
    )
    
    

    def __str__(self):
        return self.nome