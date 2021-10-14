from django.db import models

# Create your models here.
class UserModel(models.Model):
    attempt = models.CharField(max_length=50)
    dateposted = models.TimeField(null = True)
    #initally I thought I'd need to specify a user field here but I think that is handled in admin or somewhere else

    class Meta:
        verbose_name_plural = 'French App Model'
    #def __str__(self):
        #return f'{self.oventemperature}{self.dateposted}'
    