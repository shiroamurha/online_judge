from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
#from django.core.validators import MinLengthValidator
from judge.models.teste import Teste
from judge.models.problema import Problema


class Caso(Teste):

    ordem = models.IntegerField(
        default=1,
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
