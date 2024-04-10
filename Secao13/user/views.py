from django.shortcuts import render, get_object_or_404  # type: ignore
from django.views import View  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.contrib.auth import authenticate, login  # type: ignore
from user.forms import UserForm, ProfileForm
from user.models import Profile
import copy


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

        self.render = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render


class Create(ProfileBase):
    def post(self, *args, **kwargs):
        # if not self.userform.is_valid() or not self.profileform.is_valid():
        if not self.userform.is_valid():
            return self.render

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
        return self.render


class Update(View):
    ...


class Login(View):
    ...


class Logout(View):
    ...
