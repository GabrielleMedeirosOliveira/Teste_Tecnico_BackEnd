from django.db import models
import uuid


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.IntegerField()
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=25)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)