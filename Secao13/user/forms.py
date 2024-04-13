from django import forms  # type:ignore
from django.contrib.auth.models import User  # type:ignore
from django.forms import ModelForm  # type:ignore

from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {"state": 'Estado',
                  "city": 'Cidade',
                  'zip_code': 'CEP',
                  'neighborhood': 'Bairro',
                  'complement': 'Complemento',
                  'number': 'Numero',
                  'cpf': 'CPF',
                  'date_of_birth': 'Data de nascimento',
                  'age': 'Idade',
                  'address': 'Endereço',
                  }
        exclude = ('user',)


class UserForm(ModelForm):
    password = forms.CharField(
        required=False, widget=forms.PasswordInput(), label='Senha'
    )

    password2 = forms.CharField(
        required=False, widget=forms.PasswordInput(),
        label='Confirmação senha'
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',
                  'password2', 'email')

    def clean(self, *args, **kwargs):
        data = self.data  # noqa - F841
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        user_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'E-mail já cadastrado'
        error_msg_password_match = 'As senhas não conferem'
        error_msg_password_short = 'Sua senha precisa de ao menos 6 caracteres'
        error_msg_required_field = 'Este campo é obrigatório'

        if self.user:
            if user_db:
                if user_data != user_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match  # noqa - E501
                    validation_error_msgs['password2'] = error_msg_password_match  # noqa - E501

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short  # noqa - E501

        else:
            if user_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) < 6:  # type:ignore
                validation_error_msgs['password'] = error_msg_password_short

        if validation_error_msgs:
            raise forms.ValidationError(validation_error_msgs)
