from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
#from django.core.validators import MinLengthValidator
from judge.models.teste import Teste


class Exemplo(Teste):

    peso = models.IntegerField(
        default=20,
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )