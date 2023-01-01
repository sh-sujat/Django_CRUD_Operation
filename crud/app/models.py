from django.db import models


class Update(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='static/image', null=True)

    def __str__(self):
        return str(self.name)
