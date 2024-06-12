from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
