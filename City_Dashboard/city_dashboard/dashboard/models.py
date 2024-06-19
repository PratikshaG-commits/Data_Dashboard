# dashboard/models.py

from django.db import models


class CityData(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    area = models.FloatField(default=0.0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    source = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name

class Sequence(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    value = models.IntegerField(default=1)

class SequenceManager(models.Manager):
    def get_next_value(self, name):
        sequence, created = self.get_or_create(name=name)
        next_value = sequence.value
        sequence.value += 1
        sequence.save()
        return next_value
    
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)  # Use IntegerField as primary key
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # In a real application, store hashed passwords
    confirm_password = models.CharField(max_length=100)  # This should not be stored, only used for validation

    objects = models.Manager()
    sequence_manager = SequenceManager()

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.sequence_manager.get_next_value('user_id_sequence')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
