from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        self.name 


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        self.name


class Iso(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    justification = models.TextField()
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    area_hectares = models.CharField(max_length=128)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.name
