from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='judge_user_set',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='judge_user_set',  # Nome único para o relacionamento reverso
        blank=True
    )
    
    class Meta:
        verbose_name = 'User'
    


    def __str__(self):
        return self.username