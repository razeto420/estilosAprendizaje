from django.urls import path
from cuestionario import views


urlpatterns = [
    path('cuestionario',views.cuestionario,name="Cuestionario"),
]