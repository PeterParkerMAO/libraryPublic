from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    copies_available = models.IntegerField()
    pages = models.IntegerField()

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    favorite_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
