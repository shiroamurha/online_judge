from django.db import models
from judge.models.base_model import BaseModel
from judge.models.problema import Problema
from judge.models.user import User
from judge.models.linguagem import Linguagem
from django.core.validators import MinValueValidator
#from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from judge.enums.status_submission import StatusSubmission
from judge.enums.nota import Nota



class Submissao(BaseModel):

    linguagem = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=100
    )

    codigo_fonte = models.TextField(
        validators=[MinLengthValidator(1)],
        max_length=10000
    )

    status = models.TextField(
        choices=StatusSubmission.choices
    )

    submetido = models.DateTimeField()
    avaliado_em = models.DateTimeField()

    tempo_execucao_ms = models.IntegerField(
        validators=[MinValueValidator(1)]
    )

    memoria_utilizada_kb = models.IntegerField(
        validators=[MinValueValidator(32)]
    )

    nota = models.IntegerField(
        choices=Nota.choices
    )

    log_execucao = models.TextField(
        validators=[MinLengthValidator(1)],
        max_length=1000
    )

    problema = models.ForeignKey(
        Problema, on_delete=models.CASCADE
    )
    
    linguagem = models.ForeignKey(
        Linguagem, 
        on_delete=models.CASCADE
    )
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f''