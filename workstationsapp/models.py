from django.db import models


class WorkstationModel(models.Model):

    model = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'WorkstationModel'
        verbose_name_plural = 'WorkstationModels'

    def __str__(self):
        return self.model


class Workstation(models.Model):

    title = models.CharField(max_length=200)
    model = models.ForeignKey(WorkstationModel, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Workstation'
        verbose_name_plural = 'Workstations'

    def __str__(self):
        return self.title


