from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    division = models.CharField(max_length=50, verbose_name="Подразделение", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    location = models.TextField(verbose_name="Расположение", blank=True)
    logo = models.ImageField(upload_to='images/customers/logos/', null=True, blank=True, verbose_name="Логотип")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class CustomerPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=50, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание", blank=True)
    photo = models.ImageField(upload_to='images/customers/photos/', null=True, blank=True, verbose_name="Фото")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer_person', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class CustomerRequest(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    folder = models.CharField(max_length=100, verbose_name="Папка")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    person = models.ForeignKey(CustomerPerson, models.CASCADE)
    created_at = models.DateField(verbose_name="Дата создания", null=True)
    make_it_by = models.DateField(verbose_name="Дата подачи", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('customer_request', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

