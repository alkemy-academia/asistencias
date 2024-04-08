from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    # Se indica el nombre de la Tabla que se desea crear en la B.D.
    class Meta:
        db_table = 'auth_user'

    documento_identidad = models.CharField(max_length=8, unique=True)
