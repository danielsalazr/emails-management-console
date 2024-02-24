from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'employeexperience', views.EmployeeExperience)


app_name = "empleados"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    # path("listaempleado/", views.ListV.as_view(), name="listaempleado"),

    path("getMails/", views.getMails, name="getMails"),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)