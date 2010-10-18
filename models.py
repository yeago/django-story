import datetime

from django.db import models

from django.contrib import contenttypes

from django.contrib.messages.constants import DEFAULT_TAGS

MSG_CHOICES = [(v,v) for k, v in DEFAULT_TAGS.iteritems()]

class Story(models.Model):
	user = models.ForeignKey('auth.User')
	date_added = models.DateTimeField(default=datetime.datetime.now)
	expiration_date = models.DateTimeField(null=True,blank=True)
	short_description = models.TextField()
	long_description = models.TextField()
	category = models.CharField(max_length=55) # A 'key' for the type of story
	message_level = models.CharField(choices=MSG_CHOICES,max_length=15)
	content_type = models.ForeignKey('contenttypes.ContentType',null=True,blank=True)
	object_pk = models.IntegerField(null=True,blank=True)
	content_object = contenttypes.generic.GenericForeignKey()
	satisfied = models.NullBooleanField() # If this story requires an action, flag the status here
	satisfied_date = models.DateTimeField(null=True,blank=True)
	def save(self,*args,**kwargs):
		if not self.long_description:
			self.long_description = self.short_description

		if self.satisfied and not self.satisfied_date:
			self.satisfied_date = datetime.datetime.now()

		super(Story,self).save(*args,**kwargs)
