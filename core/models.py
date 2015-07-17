from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
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
	(0, 'No'),
	(1, 'Yes'),
	)

TERRAIN_CHOICES =(
	(0, 'Road'),
	(1, 'Trail'),
	(2, 'Fell'),
	(3, 'XC'),
	(4, 'Multiterrain'),
	)

DISTANCE_CHOICES = (
	(0, '1 Mile'),
	(1, '5K'),
	(2, '10K'),
	(3, '10 Miles'),
	(4, 'Half Marathon'),
	(5, 'Marathon'),
	(6, 'Other'),
	)
TSHIRT_CHOICES=(
	(0, 'No'),
	(1, 'Cotton'),
	(2, 'Technical'),
	)
PB_CHOICES=(
	(0, 'Yes'),
	(1, 'Likely'),
	(2, 'Unlikely'),
	(3, 'No'),
	)
GRADIENT_CHOICES=(
	(0, 'Flat'),
	(1, 'Slight Hills'),
	(2, 'Undulating'),
	(3, 'Hilly'),
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
	description = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	date = models.CharField(max_length=300, null=True, blank=True) 
	price = models.CharField(max_length=300, null=True, blank=True)
	distance = models.IntegerField(choices=DISTANCE_CHOICES, null=True, blank=True)
	terrain = models.IntegerField(choices=TERRAIN_CHOICES, null=True, blank=True)
	gradient = models.IntegerField(choices=GRADIENT_CHOICES, null=True, blank=True)
	medal = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	tshirt = models.IntegerField(choices=TSHIRT_CHOICES, null=True, blank=True)
	changing = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	toilets = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	water = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
	pb = models.IntegerField(choices=PB_CHOICES, null=True, blank=True)
	scenic = models.IntegerField(choices=YESNO_CHOICES, null=True ,blank=True)
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
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)


