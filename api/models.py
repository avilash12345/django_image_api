
from statistics import mode
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

#image model
class Image(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='image')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


