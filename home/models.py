from django.db import models

# Create your models here.
# category
# subcategory
# item
# slider
# Ad
# brand
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
		# one goes inside database another doesn't
STATUS = (('Active','Active'),('Inactive','Inactive'))
LABELS = (('hot','hot'),('sale','sale'),('new','new'),('','default'))

class Category(models.Model):
	title = models.CharField(max_length = 500)
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

class Slider(models.Model):
	title = models.CharField(max_length = 500)	
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
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

	def __str__(self):
		return self.title
	