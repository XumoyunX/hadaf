from django.db import models







class Courses(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.TextField()
    price = models.BigIntegerField()
    time = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    discount = models.CharField(max_length=250)

    def __str__(self):
        return self.name




class Users(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.RESTRICT)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    number =  models.CharField(max_length=250)

    def __str__(self):
        return self.name






class Gallery(models.Model):
    photo = models.ImageField(upload_to="images/")


class Teachers(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    title = models.TextField()
    telegram = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class News(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.name





