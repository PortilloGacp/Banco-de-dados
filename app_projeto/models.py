from django.db import models
from django.core.validators import RegexValidator


class data (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    celular = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Número de celular inválido.")])
    rm = models.IntegerField()
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()


