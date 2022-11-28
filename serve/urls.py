from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.services,name = 'serve-services')
]