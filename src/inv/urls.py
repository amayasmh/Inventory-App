from django.urls import path

from .views import index, home, show, add

urlpatterns =[
    path('affiche', index, name="inv_index"),
    path('', home, name="inv_home"),
    path('show/',show,name="inv_show"),
    path('add/',add,name="inv_add")
]