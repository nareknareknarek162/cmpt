from django.db import models

class User(models.Model):
    GENDERS = [('M', 'Мужской'), ('F', 'Женский')]
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    password = models.CharField(max_length=50)

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.DateTimeField()
    image = models.ImageField(upload_to='/photos/%Y/%m/%d')

class Likes(models.Model):  #manytomanyfields?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField()
