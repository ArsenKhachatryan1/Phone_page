from django.db import models

# Create your models here.


class Phone(models.Model):

    name = models.CharField('Phone name', max_length=60)
    img = models.ImageField('Phone image', upload_to='images')
    price = models.PositiveBigIntegerField('Phone price')
    date = models.DateTimeField('Phone date', auto_now=True)
    check_1 = models.BooleanField('Yes/No', null=True)
    about = models.TextField('Phone about', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        ordering = ['-date']
    

class ContactUs(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    phone = models.CharField('User name', max_length=50)
    message = models.TextField('User message')

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self) -> str:
        return self.name