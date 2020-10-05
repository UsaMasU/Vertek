from django.db import models
from django.urls import reverse


class Department(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    logo = models.ImageField(upload_to='images/departments/logos/', null=True, blank=True, verbose_name="Логотип")
    #object_case = models.ManyToManyField('DepartmentObjectCase', through='DepartmentObjects', verbose_name="Объект", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('department', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class DepartmentPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=50, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание", blank=True)
    birthday = models.DateField(verbose_name="Дата рождения", null=True)
    skill = models.TextField(blank=True, verbose_name="Умения")
    photo = models.ImageField(upload_to='images/departments/photos/', null=True, blank=True, verbose_name="Фото")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class DepartmentObjectCase(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    coefficient = models.FloatField(verbose_name="Коэффициент")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Обьект'
        verbose_name_plural = 'Обьекты'

    def __str__(self):
        return self.title


class DepartmentObjects(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    object = models.ForeignKey(DepartmentObjectCase, on_delete=models.CASCADE, verbose_name='Обьект')

    class Meta:
        verbose_name = 'Объект в предложении'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return '{0}_{1}'.format(self.department, self.object)
