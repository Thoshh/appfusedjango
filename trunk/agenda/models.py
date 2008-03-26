__doc__ = """Defines de application model"""
from django.db import models


class Person (models.Model):
    "Defines the model for the person entity"
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    comments = models.TextField()
    

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Admin:
        "Admministration configuration"
        pass

    class Meta:
        "Meta definition"
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

class Diari(models.Model):
    "Defines a model for a related table entity"
    person = models.ForeignKey(Person)
    date = models.DateField()
    comments = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.date, self.comments[:50])


    class Admin:
        "Administration configuration"
        pass

class Test(models.Model):
    "Test model entity"
    hora = models.DateTimeField()
    comments = models.TextField()
    class Admin:
        pass
