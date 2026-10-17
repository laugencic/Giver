from django.urls import path
from . import views

urlpatterns=[
    path('',views.api_calls,name="home"),
    path('movie/<int:movie_id>/',views.display,name='movie_detail'),
]