from Evaluacion_1_app import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('cuidadopersonal/', views.ProdCPersonal),
    path('dermocosmetica/', views.ProdDermo),
    path('suplementos/', views.ProdSupl),
    path('usuario/', views.Usuario),
    path('cuidadopersonal/descripcion/<str:categoria>/<str:producto>', views.Descripcion),
    path('dermocosmetica/descripcion/<str:categoria>/<str:producto>', views.Descripcion),
    path('suplementos/descripcion/<str:categoria>/<str:producto>', views.Descripcion)


]
