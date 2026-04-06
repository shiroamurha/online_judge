from django.db import models
from judge.models.base_model import BaseModel
from judge.models.user import User
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from judge.enums.genero import Genero
from judge.enums.idioma import Idioma



class Perfil(BaseModel):

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )

    data_nascimento = models.DateField(
        validators=[
            MaxValueValidator(
                date.today() - relativedelta(years=10)
            )
        ]
    )

    pais = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=100
    )

    genero = models.TextField(
        choices=Genero.choices
    )

    pagina_pessoal = models.URLField(
        validators=[MinLengthValidator(15)],
        max_length=150,
        null=True
    )

    biografia = models.TextField(
        null=True
    )

    idioma = models.TextField(
        choices=Idioma.choices
    )

    premium = models.BooleanField(
        default=False
    )

    membro_desde = models.DateField(
        default = date.today()
    )

    instituicao = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=120
    )

    posicao_ranking = models.IntegerField(
        validators=[MinValueValidator(1)]
    )

    resolvidos = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    submetidos = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    treinador = models.BooleanField(
        default=False
    )



    def __str__(self):
        return f"Perfil de {self.user}"
