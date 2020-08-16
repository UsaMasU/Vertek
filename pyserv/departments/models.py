from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to='images/departments/logos/', null=True, blank=True, verbose_name="Логотип")
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title


class DepartmentPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=50, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    skill = models.TextField(blank=True, verbose_name="Умения")
    photo = models.ImageField(upload_to='images/departments/photos/', null=True, blank=True, verbose_name="Фото")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return self.name


class DepatrmentObjectCase(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    coefficient = models.FloatField(verbose_name="Коэффициент")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обьект'
        verbose_name_plural = 'Обьекты'

    def __str__(self):
        return self.title

