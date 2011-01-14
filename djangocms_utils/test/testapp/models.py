from django.db import models
from cms.models.fields import PlaceholderField
from djangocms_utils.fields import M2MPlaceholderField

class MultiplePlaceholdersExample(models.Model):
    
    heading = models.CharField(max_length=25)
    placeholders = M2MPlaceholderField(placeholders=('first', 'second'))
    
    def __unicode__(self):
        return self.heading

class PlaceholderAsExample(models.Model):
    
    heading = models.CharField(max_length=25)
    placeholder = PlaceholderField('main')
    
    def __unicode__(self):
        return self.heading