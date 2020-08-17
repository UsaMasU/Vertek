from django.db import models
from departments.models import DepatrmentObjectCase

OFFER_TYPE = (
    ('co', 'Commercial offer'),
    ('bo', 'Bussines offer'),
)

class CommercialOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    code = models.CharField(max_length=30, verbose_name="Код предложения")
    type = models.CharField(max_length=30, choices=OFFER_TYPE, default='co')
    project_hh = models.DecimalField(verbose_name="Часы на проектирование")
    commisioning_hh = models.DecimalField(verbose_name="Часы на пусконаладку")
    project_cost = models.FloatField(verbose_name="Стоимость проектирования")
    commisioning_cost = models.FloatField(verbose_name="Стоимость пусконаладки")
    material_cost = models.FloatField(verbose_name="Стоимость материалов")
    total_cost = models.FloatField(verbose_name="Обащая стоимость")
    object_case = models.ForeignKey('ObjectBase', verbose_name="Объект")
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Предложенеие'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f'{self.code}_{self.title}'


class ObjectBase(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    quantity = models.DecimalField(verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.title


class DepartmentOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    code = models.CharField(max_length=30, verbose_name="Код предложения")
    type = models.CharField(max_length=30, choices=OFFER_TYPE, default='co')
    project_hh = models.DecimalField(verbose_name="Часы на проектирование")
    commisioning_hh = models.DecimalField(verbose_name="Часы на пусконаладку")
    object_case = models.ForeignKey(DepatrmentObjectCase, verbose_name="Объект")
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Предложенеие отдела'
        verbose_name_plural = 'Предложения отделов'

    def __str__(self):
        return f'{self.code}_{self.title}'
