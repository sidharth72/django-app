from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import time
import wikipedia as wk
from django.views.generic import ListView,DetailView
from .models import Post,Profile
from django.http import JsonResponse
import re


# Create your views here.

class PostList(ListView):

	model = Post

class PostDetail(DetailView):
	model = Post


class ProfileDetail(DetailView):
	model = Profile
	template = 'blogapp/profile_detail.html'
	slug_field = 'name'
	slug_url_kwarg = 'name'





def home(request):

	return render(request,'home.html')

def likeView(request):

	if request.method == "GET":
		i = request.GET.get('i',None)
		p = Post.objects.get(id=i)
		p.likes=p.likes+1
		p.save()
		context = {"i":p.likes}

	return JsonResponse(context)


def search(request):

	if request.method == "GET":

		search = request.GET.get("search")
		search_datas = Post.objects.all()

		for search_data in search_datas:
		

			if search in search_data.title or search in search_data.blog:

				search_results = {

					"search_datas":search_datas,
					"search":search,
					"search_data":search_data

					}
				return render(request,'search.html',search_results)

				
			elif search == None:

				return redirect('/')

		wiki_data = wk.summary(search)
	
		results = 0
		return render(request,"search.html",{"search":search,"results":results,"summary":wiki_data})




def register(request):


	if request.method == "POST":
		first_name = request.POST.get('first_name')
		username = request.POST.get("username")
		password1 = request.POST.get("password1")
		password2 = request.POST.get('password2')

		print(type(password1))

		if len(password1) < 7:

			messages.info(request,"Password must be atleast 8 characters with symbols , numbers and letters")
			return redirect('register')

		else:

			username_pattern = re.findall("\s",username)


			if password1 == password2:
				if User.objects.filter(username = username).exists():
					messages.info(request,"Username already exists")
		
				elif  username_pattern:
					messages.info(request,'Username not available')

				elif User.objects.filter(email=username).exists():
					messages.info(request,'Email exists')
				
				else:
					user = User.objects.create_user(first_name=first_name,username = username,email = username,password = password1)
					user.save()
					messages.info(request,"Account created")
					return redirect('/login')
				
			else:

				messages.info(request,"Password dosent match")
				return redirect('/register')

	
	return render(request,"register.html")



#Login Function 
def login(request):

	if request.method=="POST":
		login_username = request.POST.get('login_username') 
		login_password = request.POST.get('login_password')


		user = auth.authenticate(password=login_password,username=login_username)

		if user is not None:
			auth.login(request,user)
			messages.info(request,"Login Success")
			return redirect('profile/'+login_username)
		else:
			messages.info(request,"Invalid Username or Password")



	return render(request,"login.html")
	

def logout(request):
	auth.logout(request)
	return redirect('/')


