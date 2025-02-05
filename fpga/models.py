from django.contrib.auth import get_user_model
from django.db import models


class ProjectsFpga(models.Model):
    title = models.CharField(max_length=80, db_column='Title', verbose_name='Название проекта')
    description = models.TextField(max_length=10000, db_column='Description', verbose_name='Описание')
    link_gh = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Link_Gh',
                               verbose_name='Ссылка на GitHub')
    link_yb = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Link_Yb',
                               verbose_name='Ссылка на Youtube')
    link_web = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Link_Web',
                                verbose_name='Ссылка на Web-сайт')
    image_1 = models.ImageField(upload_to='fpga/images/%Y/%m/%d/', default=None, blank=True, null=True,
                                db_column='Image_1', verbose_name='Изображение_1')
    image_2 = models.ImageField(upload_to='fpga/images/%Y/%m/%d/', default=None, blank=True, null=True,
                                db_column='Image_2', verbose_name='Изображение_3')
    image_3 = models.ImageField(upload_to='fpga/images/%Y/%m/%d/', default=None, blank=True, null=True,
                                db_column='Image_3', verbose_name='Изображение_3')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата создания')
    autor = models.TextField(max_length=250, default=None, blank=True, null=True, db_column='Autor',
                             verbose_name='Автор')

    class Meta:
        db_table = 'ProjectFPGA'  # имя таблицы в базе данных
        verbose_name = 'Проект'  # имя модели в единственном числе
        verbose_name_plural = 'Проекты'  # имя модели во множественном числе

    def __str__(self):
        return f'Проект {self.title}'

    def get_absolute_url(self):
        return f'/fpga/{self.pk}/detail/'


class PhotoEvent(models.Model):
    description = models.TextField(max_length=10000, db_column='Description', verbose_name='Описание')
    image_event = models.ImageField(upload_to='fpga/images/%Y/%m/%d/', default=None, blank=True, null=True,
                                    db_column='Image_event', verbose_name='Фотография события')
    upload_date_event = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата создания')

    class Meta:
        db_table = 'PhotoEvent'  # имя таблицы в базе данных
        verbose_name = 'Фотография'  # имя модели в единственном числе
        verbose_name_plural = 'Фотографии'  # имя модели во множественном числе

    def __str__(self):
        return f'Фотография {self.description}'
