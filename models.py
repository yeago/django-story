from django.db import models

from django.contrib import contenttypes

from django.contrib.messages.constants import DEFAULT_TAGS

MSG_CHOICES = [((v,v) for k, v in DEFAULT_TAGS)]

class Story(models.Model):
	user = models.ForeignKey('auth.User')
	short_description = models.TextField()
	long_description = models.TextField()
	category = models.CharField() # A 'key' for the type of story
	message_level = models.CharField(choices=MSG_CHOICES)
	content_type = models.ForeignKey('contenttypes.ContentType',null=True,blank=True)
	object_pk = models.IntegerField(null=True,blank=True)
	content_object = contenttypes.models.GenericForeignKey()
	satisfied = models.NullBooleanField() # If this story requires an action, flag the status here
