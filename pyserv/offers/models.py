from django.db import models

from customers.models import CustomerRequest
from departments.models import Department, DepartmentObjectCase

OFFER_TYPE = (
    ('co', 'Commercial offer'),
    ('bo', 'Business offer'),
)


class CommercialOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    code = models.CharField(max_length=30, verbose_name="Код предложения")
    type = models.CharField(max_length=30, choices=OFFER_TYPE, default='co')
    project_hh = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Часы на проектирование", blank=True)
    commissioning_hh = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Часы на пусконаладку", blank=True)
    project_cost = models.FloatField(verbose_name="Стоимость проектирования", blank=True)
    commissioning_cost = models.FloatField(verbose_name="Стоимость пусконаладки", blank=True)
    material_cost = models.FloatField(verbose_name="Стоимость материалов", blank=True)
    total_cost = models.FloatField(verbose_name="Обащая стоимость", blank=True)
    #object_case = models.ManyToManyField('ObjectCase', through='ObjectsInOffer',verbose_name="Объект", blank=True)
    department_offer = models.ManyToManyField('DepartmentOffer', through='DepartmentInCommercial',
                                              verbose_name="Предложение отдела", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Предложенеие'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f'{self.code}-{self.title}'


class ObjectCase(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    #offer = models.ForeignKey('DepartmentOffer', on_delete=models.CASCADE, verbose_name="Предложение", null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отдел", null=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    object_code = models.CharField(max_length=50, verbose_name="Код обьекта", null=True, blank=True)
    coefficient = models.FloatField(verbose_name="Коэффициент", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Объект предложения'
        verbose_name_plural = 'Объекты предложения'

    def __str__(self):
        return self.title


class DepartmentOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    code = models.CharField(max_length=30, verbose_name="Код предложения")
    type = models.CharField(max_length=30, verbose_name="Тип", choices=OFFER_TYPE, default='co')
    request = models.ForeignKey(CustomerRequest, on_delete=models.SET_NULL, verbose_name="Запрос", null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name="Отдел", null=True)
    department_object = models.ManyToManyField(DepartmentObjectCase, through='DepObjectsInOffer', verbose_name="Обьект")
    object = models.ManyToManyField(ObjectCase, through='ObjectsInOffer', verbose_name="Дополнительный обьект")
    project_hh = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Часы на проектирование", null=True, blank=True)
    commissioning_hh = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Часы на пусконаладку", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Предложенеие отдела'
        verbose_name_plural = 'Предложения отделов'

    def __str__(self):
        return f'{self.code}_{self.title}'


class ObjectsInOffer(models.Model):
    offer = models.ForeignKey(DepartmentOffer, on_delete=models.CASCADE, verbose_name='Предложение')
    object = models.ForeignKey(ObjectCase, on_delete=models.CASCADE, verbose_name='Объект')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    manhours = models.DecimalField(verbose_name='ч/ч', max_digits=10, decimal_places=0, null=True, blank=True)
    quantity = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Объект в предложении'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return '{0}_{1}'.format(self.offer, self.object)


class DepObjectsInOffer(models.Model):
    offer = models.ForeignKey(DepartmentOffer, on_delete=models.CASCADE, verbose_name='Предложение')
    object = models.ForeignKey(DepartmentObjectCase, on_delete=models.CASCADE, verbose_name='Объект')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    manhours = models.DecimalField(verbose_name='ч/ч', max_digits=10, decimal_places=0)
    quantity = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Объект в предложении'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return '{0}_{1}'.format(self.offer, self.object)


class DepartmentInCommercial(models.Model):
    commercial_offer = models.ForeignKey(CommercialOffer, on_delete=models.CASCADE, verbose_name='Предложение')
    department_offer = models.ForeignKey(DepartmentOffer, on_delete=models.CASCADE, verbose_name='Предложение отдела')
    quantity = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Предложении отдела'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return '{0}_{1}'.format(self.commercial_offer, self.department_offer)


