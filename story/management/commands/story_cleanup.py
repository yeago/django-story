#!/usr/bin/env python
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

class Command(BaseCommand):
	def handle(self,**options):
		from story.models import Story
		Story.objects.filter(date_added__lte=datetime.now() - timedelta(days=14)).delete()
