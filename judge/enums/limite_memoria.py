from django.db import models



class LimiteMemoria(models.TextChoices):
    MB8 = "8", "8 MB"
    MB16 = "16", "16 MB"
    MB32 = "32", "32 MB"
    MB64 = "64", "64 MB"
    MB128 = "128", "128 MB"
    MB256 = "256", "256 MB"