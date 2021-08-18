from django.db import models
from django.urls import reverse

# Create your models here.
# category
# subcategory
# item
# slider
# Ad
# brand
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
		# one goes inside database another doesn't
STATUS = (('active','active'),('','inactive'))
LABELS = (('hot','hot'),('sale','sale'),('new','new'),('','default'))

class Category(models.Model):
	title = models.CharField(max_length = 500)
	status = models.CharField(max_length = 50, choices=STATUS,blank = True)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')

	def __str__(self):
		return self.title

class SubCategory(models.Model):
	title = models.CharField(max_length = 500)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	category = models.ForeignKey(Category,on_delete = models.CASCADE)

	def __str__(self):
		return self.title
	def get_url(self):
		return reverse("home:subcategory",kwargs={'slug':self.slug}) # yo name ko slug transfer garinxa			


class Brand(models.Model):
	title = models.CharField(max_length = 500,blank=True)
	status = models.CharField(max_length = 50, choices=STATUS,blank = True)
	slug = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	

	def __str__(self):
		return self.title	
	def get_url(self):
		return reverse("home:brand",kwargs={'slug':self.slug})


class Slider(models.Model):
	title = models.CharField(max_length = 500)	
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	status = models.CharField(max_length = 50, choices=STATUS,blank = True)
	def __str__(self):
		return self.title

class Item(models.Model):
	title = models.CharField(max_length=400)
	slug = models.CharField(max_length = 500)
	price = models.IntegerField() #default holds  11 digits kind of
	discounted_price = models.IntegerField(blank = True)
	image = models.ImageField(upload_to = 'media')
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
	stock = models.CharField(max_length = 50, choices = STOCK)
	status = models.CharField(max_length = 50, choices=STATUS,blank = True)
	labels = models.CharField(max_length = 50, choices=LABELS,blank = True)
	brand = models.ForeignKey(Brand, null=True,on_delete = models.CASCADE)

	def __str__(self):
		return self.title
	def get_url(self):
		return reverse("home:detail",kwargs={'slug':self.slug})	

	
class Ad(models.Model):
	title = models.CharField(max_length = 500)
	slug = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField(unique = True) # yo part ma everytime value unique auxa so true hunxa

	def __str__(self):
		return self.title	

	

	

class Review(models.Model):
	name = models.CharField(max_length=400)
	email = models.CharField(max_length=400)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	slug = models.CharField(max_length = 400)

	
	def __str__(self):
		return self.name





   