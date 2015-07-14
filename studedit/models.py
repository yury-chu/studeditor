from django.db import models

# Create your models here.


class Senders(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return ' '.join([
            self.name,
            self.role,
        ])


class Groups(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)
    year = models.DateField(auto_now=True)

    def __unicode__(self):
        return ' '.join([
            self.name,
            self.faculty,
            #self.year,
        ])


class Students(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    group = models.ForeignKey(Groups)
    sender = models.ForeignKey(Senders)

    def __unicode__(self):
        return ' '.join([
            self.name,
            self.family,
            self.group,
            self.sender,
        ])
