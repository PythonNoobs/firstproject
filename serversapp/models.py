from django.db import models


# Create your models here.

class ServerModel(models.Model):
    servermodelname = models.CharField(max_length=100)


class Server(models.Model):
    name = models.CharField(max_length=50)
    netbiosname = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    macadress = models.GenericIPAddressField()
    manufacturer = models.CharField(max_length=50, choices={})
    formfactor = models.CharField(max_length=50, choices={})
    type = models.CharField(max_length=50)
    servermodel_id = models.ForeignKey(ServerModel, on_delete=models.CASCADE)
    # technic_id = models.ForeignKey(Technic)
