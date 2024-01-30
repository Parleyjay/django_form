from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30) 
    email = models.EmailField('User Email')
    phone = models.CharField('Contact Phone', max_length = 25)

    def __str__(self):
       return self.first_name + ' ' + self.last_name

     
