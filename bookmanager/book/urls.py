from django.urls import path
from django.urls import register_converter
from converters import MobileConverter
from book.views import *


register_converter(MobileConverter, 'mobile')

urlpatterns = [
    path('index/', index),
    path('<int:id1>/<mobile:id2>/', shop),
    path('form/', post),
    path('json/', post_json),
    path('response/', response),
    path('redirect/', test_redirect),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),
    path('loginclass/', LoginView.as_view()),

]