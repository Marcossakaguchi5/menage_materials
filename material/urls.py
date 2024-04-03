# urls.py
from django.urls import path
from material_app import views
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.lista_materiais, name='lista_materiais'),
    path('adiciona/', views.adiciona_material, name='adiciona_material'),
    path('edita/<int:pk>/', views.edita_material, name='edita_material'),
    path('deleta/<int:pk>/', views.deleta_material, name='deleta_material'),
]


