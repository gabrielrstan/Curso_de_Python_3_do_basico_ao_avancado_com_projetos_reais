import copy

from django.contrib import messages  # type: ignore
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.shortcuts import (get_object_or_404, redirect,  # type: ignore
                              render)
from django.views import View  # type: ignore

from user.forms import ProfileForm, UserForm
from user.models import Profile


class ProfileBase(View):
    template_name = 'user/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.cart = copy.deepcopy(self.request.session.get('cart', {}))
        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = Profile.objects.filter(
                user=self.request.user).first()

            self.context = {
                'userform': UserForm(
                    data=self.request.POST or None, user=self.request.user,
                    instance=self.request.user,),
                'profileform': ProfileForm(
                    data=self.request.POST or None, instance=self.profile)
            }
        else:
            self.context = {
                'userform': UserForm(data=self.request.POST or None),
                'profileform': ProfileForm(data=self.request.POST or None)
            }

        self.userform = self.context['userform']
        self.profileform = self.context['profileform']

        if self.request.user.is_authenticated:
            self.template_name = 'user/update.html'

        self.render_ = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render_


class Create(ProfileBase):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.profileform.is_valid():
            messages.error(
                self.request,
                'Por favor, preencha os campos corretamente.'
            )
            return self.render_

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        if self.request.user.is_authenticated:

            user = get_object_or_404(User,
                                     username=self.request.user.username)  # type: ignore # noqa - E501
            user.username = username
            if password:
                user.set_password(password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if not self.profile:
                self.profileform.cleaned_data['user'] = user
                profile = Profile(**self.profileform.cleanned_data)
                profile.save()
            else:
                profile = self.profileform.save(commit=False)
                profile.user = user
                profile.save()

        else:
            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.user = user
            profile.save()

        if password:
            authentic = authenticate(
                self.request, username=user, password=password
            )

            if authentic:
                login(self.request, user=user)

        self.request.session['cart'] = self.cart
        self.request.session.save()

        messages.success(self.request,
                         'Seu cadastro foi criado ou atualizado com sucesso')

        return redirect('product:cart')


class Update(View):
    ...


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('user:create')

        user = authenticate(
            self.request, username=username, password=password)

        if not user:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('user:create')

        login(self.request, user=user)

        messages.success(self.request, 'Você foi logado com sucesso')

        return redirect('product:cart')


class Logout(View):
    def get(self, *args, **kwargs):
        cart = copy.deepcopy(self.request.session.get('cart', {}))

        logout(self.request)

        self.request.session['cart'] = cart
        self.request.session.save()

        messages.success(self.request, 'Você foi deslogado com sucesso')
        return redirect('product:list')
