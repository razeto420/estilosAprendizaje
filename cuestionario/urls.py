from django.urls import path
from cuestionario import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home,name="Home"),
    path('pregunta/',views.Pregunta,name="Pregunta"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)