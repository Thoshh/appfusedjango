from django.db import models

class Person (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    comments = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (first_name, last_name)

    class Admin:
        pass

    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Personas'
