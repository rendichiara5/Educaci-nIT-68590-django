from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="país")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural = "países"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(
        Pais, null=True, blank=True, on_delete=models.CASCADE, verbose_name="país de origen"
    )

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
