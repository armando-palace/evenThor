from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class Event(models.Model):
  """Evento."""
  name = models.CharField(max_length=255, unique=True)
  date = models.DateField()

  def __str__(self):
    return self.name

class Presentation(models.Model):
  """Ponencia."""
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, unique=True)
  date = models.DateField()
  time = models.TimeField()
  duration = models.DurationField()
  
  def __str__(self):
    return self.name

class Speaker(models.Model):
  """Ponente"""
  presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  position = models.CharField(max_length=128)
  organization = models.CharField(max_length=128)

  def __str__(self):
    return self.name

class Assistant(models.Model):
  """Asistente"""
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  phone = models.CharField(max_length=32)
  email = models.EmailField(max_length=255)
  organization = models.CharField(max_length=128)


class Profile(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  ROLES = (('ADM', 'Adminitrador'), ('GER', 'Gerente'),('AGN', 'Agente'))
  role = models.CharField(max_length=3, choices=ROLES, default='ADM')

  class Meta:

      permissions = (
        ('is_admin', _('Is Admin')),
        ('is_manager', _('Is Manager')),
        ('is_agent', _('Is Agent')),
      )

  def __str__(self):
    cadena = "{0} => {1}"
    return cadena.format(self.usuario.username, self.role)

