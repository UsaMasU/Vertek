from django.db import models
from departments.models import Department

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
    object_case = models.ManyToManyField('ObjectCase', through='ObjectsInOffer',
                                         verbose_name="Объект", blank=True)
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
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.title


class ObjectsInOffer(models.Model):
    offer = models.ForeignKey(CommercialOffer, on_delete=models.CASCADE, verbose_name='Предложение')
    object = models.ForeignKey(ObjectCase, on_delete=models.CASCADE, verbose_name='Объект')
    quantity = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Объект в предложении'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return '{0}_{1}'.format(self.offer, self.object)


class DepartmentOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    code = models.CharField(max_length=30, verbose_name="Код предложения")
    type = models.CharField(max_length=30, verbose_name="Тип", choices=OFFER_TYPE, default='co')
    project_hh = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Часы на проектирование", blank=True)
    commissioning_hh = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Часы на пусконаладку", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Предложенеие отдела'
        verbose_name_plural = 'Предложения отделов'

    def __str__(self):
        return f'{self.code}_{self.title}'


class DepartmentInCommercial(models.Model):
    commercial_offer = models.ForeignKey(CommercialOffer, on_delete=models.CASCADE, verbose_name='Предложение')
    department_offer = models.ForeignKey(DepartmentOffer, on_delete=models.CASCADE, verbose_name='Предложение отдела')
    quantity = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Предложении отдела'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return '{0}_{1}'.format(self.commercial_offer, self.department_offer)


