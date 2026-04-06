from django.db import models



class Genero(models.TextChoices):
    MAN = "MAN", "Homem"
    WOMAN = "WOMAN", "Mulher"
    NON_BINARY = "NON_BINARY", "Não binário"
    NOT_INFORMED = "NOT_INFORMED", "Não informado"
    