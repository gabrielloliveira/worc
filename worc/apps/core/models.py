import uuid

from django.core.validators import MinValueValidator
from django.db import models

from worc.apps.core.validators import validate_cpf


class BaseModel(models.Model):
    """
    Base model with common fields
    """

    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)
    uuid = models.UUIDField("UUID", unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Candidate(BaseModel):
    """
    Candidate model
    """

    name = models.CharField("nome", max_length=500)
    email = models.EmailField("email", max_length=500, unique=True)
    cpf = models.CharField("CPF", max_length=14, unique=True, validators=[validate_cpf])
    age = models.IntegerField("idade", validators=[MinValueValidator(18)])
    salary_claimed = models.DecimalField(
        "pretenção salarial", max_digits=10, decimal_places=2, blank=True, null=True
    )
    immediate_availability = models.BooleanField(
        "disponibilidade imediata", default=False
    )

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.name
