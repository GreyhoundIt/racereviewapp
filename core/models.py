from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField
import os
import uuid

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
	)

YESNO_CHOICES =(
	('No', 'No'),
	('Yes', 'Yes'),
	)

TERRAIN_CHOICES =(
	('Road', 'Road'),
	('Trail', 'Trail'),
	('Fell', 'Fell'),
	('XC', 'XC'),
	('Multiterrain', 'Multiterrain'),
	)

DISTANCE_CHOICES = (
	('1 Mile', '1 Mile'),
	('5K', '5K'),
	('10K', '10K'),
	('10 Miles', '10 Miles'),
	('Half Marathon', 'Half Marathon'),
	('Marathon', 'Marathon'),
	('Other', 'Other'),
	)
TSHIRT_CHOICES=(
	('No', 'No'),
	('Cotton', 'Cotton'),
	('Technical', 'Technical'),
	)
PB_CHOICES=(
	('Yes', 'Yes'),
	('Likely', 'Likely'),
	('Unlikely', 'Unlikely'),
	('No', 'No'),
	)
GRADIENT_CHOICES=(
	('Flat', 'Flat'),
	('Slight Hills', 'Slight Hills'),
	('Undulating', 'Undulating'),
	('Hilly', 'Hilly'),
	)

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)


# Create your models here.
class Race(models.Model):
	title = models.CharField(max_length=300)
	website = models.CharField(max_length=300, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	position = GeopositionField(null=True, blank=True)
	date = models.CharField(max_length=300, null=True, blank=True) 
	price = models.CharField(max_length=300, null=True, blank=True)
	distance = models.CharField(choices=DISTANCE_CHOICES,max_length=300, null=True, blank=True)
	terrain = models.CharField(choices=TERRAIN_CHOICES, max_length=300,null=True, blank=True)
	gradient = models.CharField(choices=GRADIENT_CHOICES,max_length=300, null=True, blank=True)
	medal = models.CharField(choices=YESNO_CHOICES,max_length=300, null=True, blank=True)
	tshirt = models.CharField(choices=TSHIRT_CHOICES, max_length=300, null=True, blank=True)
	changing = models.CharField(choices=YESNO_CHOICES,max_length=300, null=True, blank=True)
	toilets = models.CharField(choices=YESNO_CHOICES,max_length=300, null=True, blank=True)
	water = models.CharField(choices=YESNO_CHOICES,max_length=300, null=True, blank=True)
	pb = models.CharField(choices=PB_CHOICES,max_length=300, null=True, blank=True)
	scenic = models.CharField(choices=YESNO_CHOICES,max_length=300, null=True ,blank=True)
	image_file = models.ImageField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname='race_list', args=[self.id])

	def get_average_rating(self):
		average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
		if average == None:
			return average
		else:
			return int(average)


	def get_reviews(self):
		return self.review_set.all()

class Review(models.Model):
	race = models.ForeignKey(Race)
	user = models.ForeignKey(User)
	review = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True, verbose_name='Overall Raiting')
	valueformoney = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True, verbose_name='Value for money')
	goodybag = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True, verbose_name='Goody Bag')
	atmosphere = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)


