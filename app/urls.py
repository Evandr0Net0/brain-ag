from django import views
from django.contrib import admin
from django.urls import path
from producers.views import index, ProducersListView, NewProducerCreateView, ProducerDetailView, ProducerUpdateView, ProducerDeleteView, retorna_total_area, retorna_total_arable_area, retorna_total_vegetation_area, retorna_total_prod, relatorio_estado, relatorio_areas_agric_veget,relatorio_cultura
from django.conf.urls.static import static
from django.conf import settings
from producers.models import Producer
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='index'),
    path('new_producer/', NewProducerCreateView.as_view(model=Producer,
         success_url="/producers/"), name='new_producer'),
    path('producers/', ProducersListView.as_view(), name='producers'),
    path('producer/<int:pk>/', ProducerDetailView.as_view(), name='producer_detail'),
    path('producer/<int:pk>/update',
         ProducerUpdateView.as_view(), name='producer_update'),
    path('producer/<int:pk>/delete',
         ProducerDeleteView.as_view(), name='producer_delete'),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('retorna_total_area', retorna_total_area, name="dash_total_area"),
    path('retorna_total_arable_area', retorna_total_arable_area,
         name="dash_total_arable_area"),
    path('retorna_total_vegetation_area', retorna_total_vegetation_area,
         name="dash_total_vegetation_area"),
    path('retorna_total_prod', retorna_total_prod, name="dash_total_prod"),
    path('relatorio_estado', relatorio_estado, name="relatorio_estado"),
    path('relatorio_areas_agric_veget', relatorio_areas_agric_veget,
         name="relatorio_areas_agric_veget"),
    path('relatorio_cultura', relatorio_cultura,
         name="relatorio_cultura"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
