from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProjectsFpga, PhotoEvent


@admin.register(ProjectsFpga)
class ProjectsFpgaAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = ('id', 'title', 'description', 'autor', 'link_gh', 'link_yb', 'link_web', 'projectfpga_image_1',
                    'projectfpga_image_2', 'projectfpga_image_3', 'upload_date')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('title', 'description', 'autor')
    # Ordering - сортировка
    ordering = ('title',)
    # List_per_page - количество элементов на странице
    list_per_page = 5
    # Поля, которые можно редактировать
    list_editable = ('title', 'description', 'autor', 'link_gh', 'link_yb', 'link_web',)
    fields = ['title', 'description', 'autor', 'link_gh', 'link_yb', 'link_web', 'image_1', 'image_2', 'image_3']

    @admin.display(description="Изображение для проекта")
    def projectfpga_image_1(self, projectfpga: ProjectsFpga):
        if projectfpga.image_1:
            return mark_safe(f'<img src="{projectfpga.image_1.url}" width="96">')
        else:
            return 'Без изображения'

    @admin.display(description="Изображение для проекта")
    def projectfpga_image_2(self, projectfpga: ProjectsFpga):
        if projectfpga.image_2:
            return mark_safe(f'<img src="{projectfpga.image_2.url}" width="96">')
        else:
            return 'Без изображения'

    @admin.display(description="Изображение для проекта")
    def projectfpga_image_3(self, projectfpga: ProjectsFpga):
        if projectfpga.image_3:
            return mark_safe(f'<img src="{projectfpga.image_3.url}" width="96">')
        else:
            return 'Без изображения'


@admin.register(PhotoEvent)
class PhotoEventAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = ('id', 'description', 'photoevent_image', 'upload_date_event')
    # Поля, которые будут ссылками
    list_display_links = ('id',)
    # Поля по которым будет поиск
    search_fields = ('description',)
    # Поля по которым будет фильтрация
    # list_filter = ('upload_date_event')
    # Ordering - сортировка
    ordering = ('upload_date_event',)
    # List_per_page - количество элементов на странице
    list_per_page = 5
    # Поля, которые можно редактировать
    list_editable = ('description',)
    fields = ['description', 'image_event']

    @admin.display(description="Фотография события")
    def photoevent_image(self, photoevent: PhotoEvent):
        if photoevent.image_event:
            return mark_safe(f'<img src="{photoevent.image_event.url}" width="96">')
        else:
            return 'Без изображения'
