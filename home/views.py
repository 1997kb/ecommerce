from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User 

# Create your views here.
class BaseView(View): # generic view inbuilt
	views = {}
	views['categories'] = Category.objects.all()
	views['subcategories'] = SubCategory.objects.all()


class HomeView(BaseView):
	def get(self,request):
		self.views['categories'] = Category.objects.all()
		self.views['sliders'] = Slider.objects.all() #updating dictoinary
		self.views['sale'] = Item.objects.filter(labels = 'sale')#sale product lai tanxa
		self.views['items'] = Item.objects.filter(status = 'active') #jasko status active teslai tanne
		self.views['brands'] = Brand.objects.all()
		self.views['ads'] = Ad.objects.all()
		return render(request,'index.html',self.views)

class SubCategoryView(BaseView):
	def get(self,request,slug):

		id = SubCategory.objects.get(slug=slug).id
		self.views['subcategory_product'] = Item.objects.filter(subcategory_id = id)
		return render(request,'subcategory.html',self.views)

class DetailView(BaseView):
	def get(self,request,slug):

		self.views['review_detail'] = Review.objects.filter(slug = slug)
		self.views['product_detail'] = Item.objects.filter(slug = slug)
		return render( request,'product-details.html',self.views)

def review(request):
	if request.method == 'POST':
		name = request.user.username
		email = request.user.email
		comment = request.POST['comment']
		slug = request.POST['slug']
		data = Review.objects.create(
				name = name,
				email = email,
				comment = comment,
				slug = slug
			)
		data.save()
	return redirect(f'/detail/{slug}')   #redirect to same page	

class BrandView(BaseView):
	def get(self,request,slug):

		
		id = Brand.objects.get(slug=slug).id
		self.views['brand_product'] = Item.objects.filter(brand_id = id)
		return render(request,'brand.html',self.views)

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		fname = request.POST['fname']
		lname = request.POST['lname']

		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,'The username is already taken')
				return render(request,'signup.html')
			elif User.objects.filter(email = email).exists():
				messages.error(request,'The email is already taken')
				return render(request,'signup.html')
			else:
				user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = fname,
                    last_name = lname 
				)
				user.save()
				messages.success(request,'you are registered')
				return render(request,'signup.html')
		else:
			messages.error(request,'The password does not match')
			return render(request,'signup.html')
	return render(request,'signup.html')

def add_to_cart(request):
	if request.method == 'POST':
		slug = request.POST['slug']
		quantity = request.POST['quantity']
		user = request.user.username
		items = Item.objects.filter(slug = slug)[0]
		price = Item.objects.get(slug = slug).price
		total = int(price) * int(quantity)
		data = Cart.objects.create(
			user = user,
			slug = slug,
			quantity = quantity,
			items = items,
			total = total


			)
		data.save()
		return redirect('/cart')

class CartView(BaseView):
	def get(self,request):
		self.views['my_cart'] = Cart.objects.filter(user = request.user.username,checkout = False)


		return render(request,'cart.html',self.views)




		


        
         