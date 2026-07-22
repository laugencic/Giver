from . import views
from django.urls import path

urlpatterns=[
    path('chat/',views.chat,name="chat"),
    path('details/',views.details,name='details')
]