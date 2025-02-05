from django.urls import path
from . import views

app_name = 'fpga'
urlpatterns = [
    path('projects/', views.ProjectsFpgaCatalogView.as_view(), name='catalog'),  # каталог fpga_проектов
    path('<int:pk>/detail/', views.FpgaProjectDetailView.as_view(), name='detail_project_by_id'),    # Детальная страница acaны по pk
    path('photo_events/', views.FotoEventsView.as_view(), name='photo_events'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),# каталог fpga_проектов
]
