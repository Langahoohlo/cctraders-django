from django.db import models

# Create your models here.

class ServiceOne(models.Model):
    serviceName = models.CharField(max_length=100)
    servicceDescription = models.TextField()

def save(self, *args, **kwargs):
        # Ensure there's only one instance of ServiceOne
        if ServiceOne.objects.exists():
            existing_instance = ServiceOne.objects.first()
            existing_instance.delete()

        return super(ServiceOne, self).save(*args, **kwargs)

class ServiceTwo(models.Model):
    serviceName = models.CharField(max_length=100)
    servicceDescription = models.TextField()

class ServiceThree(models.Model):
    serviceName = models.CharField(max_length=100)
    servicceDescription = models.TextField()

    def __str__(self):
        return self.name