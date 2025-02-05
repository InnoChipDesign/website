from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from .models import ProjectsFpga, PhotoEvent
from django.db.models import Q


class PageNotFoundView(TemplateView):
    template_name = 'fpga/404.html'


class IndexView(TemplateView):
    """
    Класс (статический) для отображения страницы "О нас"
    """
    template_name = 'fpga/main.html'


class ProjectsFpgaCatalogView(ListView):
    """
    Класс (динамический с пагинацией) для отображения страницы каталога проектов FPGA
    """
    model = ProjectsFpga  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'fpga/projects.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'projects'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 4  # Количество объектов на странице
    extra_context = {'title': 'Каталог проектов'}  # Дополнительный контекст для передачи в шаблон

    # Метод для модификации начального запроса к БД
    def get_queryset(self):
        # Получение параметров сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'title')
        order = self.request.GET.get('order', 'desc')
        search_query = self.request.GET.get('search_query', '')

        # Определение направления сортировки
        if order == 'asc':
            order_by = f'-{sort}'
        else:
            order_by = sort

        # Фильтрация карточек по поисковому запросу и сортировка
        if search_query:
            queryset = ProjectsFpga.objects.filter(
                Q(title__iregex=search_query) |
                Q(description__iregex=search_query) |
                Q(autor__iregex=search_query)
            ).order_by(order_by).distinct()
        else:
            queryset = ProjectsFpga.objects.order_by(order_by)
        return queryset


class FpgaProjectDetailView(DetailView):
    """
    Класс для детального представления информации о проекте.
    """
    # указываем модель для представления
    model = ProjectsFpga
    # Указываем путь к шаблону для детального отображения карточки
    template_name = 'fpga/project_detail.html'
    # Переопределяем имя переменной в контексте шаблона на 'project' (до этого было 'projects')
    context_object_name = 'projectfpga'
    extra_context = {'title': 'Проект'}  # Дополнительный контекст для передачи в шаблон


class FotoEventsView(ListView):
    """
    Класс для отображения страницы "Фотогалерея"
    """
    model = PhotoEvent  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'fpga/photo_events.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'photo_events'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 6  # Количество объектов на странице
    extra_context = {'title': 'Фотогалерея'}  # Дополнительный контекст для передачи в шаблон

    def get_queryset(self):
        # Получение параметров сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date_event')
        order = self.request.GET.get('order', 'desc')

        # Определение направления сортировки
        if order == 'desc':
            order_by = f'-{sort}'
        else:
            order_by = sort

        # Фильтрация карточек по поисковому запросу и сортировка
        queryset = PhotoEvent.objects.order_by(order_by)
        return queryset


class ContactsView(TemplateView):
    """
    Класс (статический) для отображения страницы "Контакты"
    """
    template_name = 'fpga/contacts.html'
