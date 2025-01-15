from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.postgres.fields import HStoreField
from slugify import slugify
from shop.model_data import hardware_templates


class Hardware(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование", validators=[
        MinLengthValidator(5, message="Не менее 5 символов"), MaxLengthValidator(255, message="Не более 255 символов")])
    slug = AutoSlugField(
        populate_from="title",
        slugify_function=slugify,
        verbose_name="Slug",
        db_index=True,
        unique=True
    )
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              default="default.webp", blank=True, null=True, verbose_name="Фото")
    description = models.TextField(blank=True, verbose_name="Описание")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения")
    num_in_stock = models.IntegerField(default=1, verbose_name="Количество")
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, related_name='products', verbose_name="Категория")
    params = HStoreField(default=dict, verbose_name='Характеристики')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Комплектующие для ПК"
        verbose_name_plural = "Комплектующие для ПК"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    def save(self, **kwargs):
        if not self.params:
            self.params = hardware_templates[self.cat_id-1]
        super().save(**kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


