from django.db import models


# 🔹 ГРУППА (1 ко многим)
class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 🔹 КЛУБ (многие ко многим)
class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 🔹 СТУДЕНТ
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    clubs = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"