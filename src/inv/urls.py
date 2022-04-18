from django.urls import path

from .views import home, show, add

urlpatterns =[
    path('', home, name="inv_home"),
    path('show/',show,name="inv_show"),
    path('add/',add,name="inv_add")

]