from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    sales_channel = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    time_request = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
