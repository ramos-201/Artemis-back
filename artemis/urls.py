from django.http import HttpResponse
from django.urls import path

from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums
from artemis.api.account_view import register_conn_view, LoginView


def conn_view(request):
    return HttpResponse('Connection established')


urlpatterns = [
    path('conn/', conn_view, name='conn'),

    path('home/', conn_view, name=RoutesViewsEnums.HOME.value),
    path('api/login/', LoginView.as_view(), name=RoutesViewsEnums.LOGIN.value),
    path('register/', register_conn_view, name=RoutesViewsEnums.REGISTER.value)
]
