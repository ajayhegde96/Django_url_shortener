from django.db import models
from .utils import code_generator
# Create your models here.

class URL_short(models.Model):
	url 		 = models.CharField(max_length=220, )
	shortcode 	 = models.CharField(max_length=15,unique=True,blank=True)
	updated_time = models.DateTimeField(auto_now=True)#everytime model is updated and saved
	timestamp	 = models.DateTimeField(auto_now_add=True)#when model is created
	#empty_datetime = models.DateTimrField(auto_now=False , auto_now_add=False)
	#shortcode = models.CharField(max_length=15,null=True)
	#shortcode = models.CharField(max_length=15, default='defaultsc')

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode== "":
			self.shortcode=	code_generator()
		super(URL_short, self).save(*args, **kwargs)

	def __str__(self):
	 	return str(self.url)

	def __unicode__(self):
		return str(self.url)




'''
Run these commands if any changes are made here!!

1. python manage.py makemigrations

2. python manage.py migrate

'''