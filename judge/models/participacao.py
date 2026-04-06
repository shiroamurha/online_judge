from django.db import models
from judge.models.competicao import Competicao
from judge.models.base_model import BaseModel
from judge.models.user import User
from django.core.validators import MinValueValidator



class Participacao(BaseModel):

    registro = models.DateTimeField()

    oficial = models.BooleanField(default=True)

    total_pontos = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)]
    )

    competicao = models.ForeignKey(
        Competicao, 
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.competicao}"