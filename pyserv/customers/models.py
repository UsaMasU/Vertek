from django.db import models


class Customer(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    location = models.TextField(verbose_name="Расположение")
    logo = models.ImageField(upload_to='images/customers/logos/', null=True, blank=True, verbose_name="Логотип")
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.title


class CustomerPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=50, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='images/customers/photos/', null=True, blank=True, verbose_name="Фото")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class CustomerRequest(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    folder = models.CharField(max_length=100, verbose_name="Папка")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    person = models.ForeignKey(CustomerPerson, models.CASCADE)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.title
