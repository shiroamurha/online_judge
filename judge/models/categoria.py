from django.db import models
from judge.models.base_model import BaseModel
#from django.core.validators import MinValueValidator
#from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator



class Categoria(BaseModel):

    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)]
    )

    slug = models.SlugField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        unique=True
    )

    descricao = models.TextField(
        null=True
    )

    def __str__(self):
        return self.nome
    