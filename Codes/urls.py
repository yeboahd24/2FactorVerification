from django.urls import path
from .views import home_page, verification, authentication_view


urlpatterns = [
    path('', home_page, name='home'),
    path('authenticate/', authentication_view, name='authenticate'),
    path('verification/', verification, name='verify'),

]
