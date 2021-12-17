from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("blog/analyze",views.analyze,name="analyze")
]
