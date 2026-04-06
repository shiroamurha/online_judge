from django.db import models



class StatusSubmission(models.TextChoices):
    NOT_ANSWERED = "NOT_ANSWERED", "Não Respondida"
    IN_QUEUE = "IN_QUEUE", "Em fila de execução"
    RUNNING = "RUNNING", "Execução"
    ACCEPTED = "ACCEPTED", "Aceito"
    WRONG_ANSWER = "WRONG_ANSWER", "Resposta Errada"
    TIME_LIMIT_EXCEEDED = "TIME_LIMIT_EXCEEDED", "Tempo Limite Excedido"
    MEMORY_LIMIT_EXCEEDED = "MEMORY_LIMIT_EXCEEDED", "Limite de Memória Excedido"
    RUNTIME_ERROR = "RUNTIME_ERROR", "Erro de Runtime"
    COMPILATION_ERROR = "COMPILATION_ERROR", "Erro de Compilação"
    PRESENTATION_ERROR = "PRESENTATION_ERROR", "Erro de Apresentação"
    INTERNAL_ERROR = "INTERNAL_ERROR", "Erro Interno"