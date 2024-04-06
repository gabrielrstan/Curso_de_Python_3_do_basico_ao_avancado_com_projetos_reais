from django.urls import path  # type: ignore
from user.views import Create, Update, Login, Logout

app_name = 'user'

urlpatterns = [
    path('', Create.as_view(), name='create'),
    path('update/', Update.as_view(), name='update'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
