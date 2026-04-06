from django.db import models
from judge.models.base_model import BaseModel
#from django.core.validators import MinValueValidator
#from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from datetime import datetime


class Teste(BaseModel):

    nome = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(80)]
    )

    dados_entrada = models.TextField(
        max_length=5000,
        validators=[MinLengthValidator(1)]
    )

    criado = models.DateTimeField(
        default=datetime.now()
    )
        
    atualizado = models.DateTimeField(
        default=datetime.now()
    )


    
    def __str__(self):
        return self.nome