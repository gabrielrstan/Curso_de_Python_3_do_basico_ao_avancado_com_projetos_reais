import re

from django.contrib.auth.models import User  # type: ignore
from django.db import models  # type: ignore
from django.forms import ValidationError  # type: ignore

from utils.validacpf import valida_cpf


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.user.username}'

    def clean(self):
        error_messages = {}

        sent_cpf = self.cpf or None
        saved_cpf = None
        profile = Profile.objects.filter(cpf=sent_cpf).first()

        if profile:
            saved_cpf = profile.cpf

            if saved_cpf is not None and self.pk != profile.pk:
                error_messages['cpf'] = 'CPF já cadastrado.'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'CPF inválido.'

        if re.search(r'[^0-9]', self.zip_code) or len(self.zip_code) < 8:
            error_messages['zip_code'] = 'CEP inválido.'

        if error_messages:
            raise ValidationError(error_messages)
