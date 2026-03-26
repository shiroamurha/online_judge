from django.db import models
from online_judge.models.base_model import BaseModel
from online_judge.models.linguagem import Linguagem
from django.core.validators import MinValueValidator
#from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from online_judge.enums.status_submission import StatusSubmission
from online_judge.enums.nota import Nota



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

    submissao_linguagem = models.ForeignKey(
        Linguagem, 
        on_delete=models.CASCADE,
        null=True
    )
    


    def __str__(self):
        return 'submissao? nao sei oq deveria retornar'