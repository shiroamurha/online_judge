from django.db import models
from judge.models.base_model import BaseModel
from judge.models.problema import Problema
from judge.models.competicao import Competicao
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator



class ProblemaCompeticao(BaseModel):

    label = models.CharField(
        validators=[MinValueValidator(1)],
        max_length=5
    )

    pontos = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
        default=100
    )
    
    ordem = models.IntegerField(
        validators=[MinValueValidator(1)]
    )

    problema = models.ForeignKey(
        Problema, 
        on_delete=models.CASCADE
    )

    competicao = models.ForeignKey(
        Competicao, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.label