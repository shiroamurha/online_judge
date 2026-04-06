from django.db import models
from judge.models.base_model import BaseModel
from django.core.validators import MinValueValidator
#from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator



class Linguagem(BaseModel):

    name = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=50,
        unique=True
    )

    slug = models.SlugField(
        validators=[MinLengthValidator(3)],
        max_length=50,
        unique=True
    )

    compilador = models.CharField(
        validators=[MinLengthValidator(5)],
        max_length=80
    )

    versao = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=50
    )

    multiplicador_tempo = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )

    multiplicador_memoria = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name