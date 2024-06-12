from django.db import models


class Сategory(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Торговая марка'
        verbose_name_plural = 'Торговые марки'


class Subcategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Сategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    packing = models.CharField(max_length=100)
    count_in_box = models.IntegerField()
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
