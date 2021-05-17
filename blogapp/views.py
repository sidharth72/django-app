from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import time
import wikipedia as wk
from django.views.generic import ListView,DetailView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin,FormView
from .models import Post,Profile
from .forms import UpdateProfileForm,UserForm
from django.http import JsonResponse
import re


# Create your views here.

#Post listing page
class PostList(ListView):

	model = Post

#Post detail page 	
class PostDetail(DetailView):
	model = Post
	template = 'blogapp/post_detail.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'


#Profile page of users
#class ProfileDetail(LoginRequiredMixin,FormMixin,DetailView):
#	model = Profile
#	template = 'blogapp/profile_detail.html'
#	slug_field = 'name'
#	slug_url_kwarg = 'name'
#	form_class = UpdateProfileForm
#	initial = {'key':'value'}

#	def get_success_url(self):
#		self.request.path
		
	

#	def get_queryset(self):
#		search = self.request.GET.get('search')
#		return search


#	def get_context_data(self, **kwargs):

#		context = super(ProfileDetail, self).get_context_data(**kwargs)
#		context['posts'] = Post.objects.all()

#		return context


#	def get_object(self,queryset=None):
#		return Profile.objects.get(uuid=self.kwargs.get('uuid'))

#	def post(self,request,*args,**kwargs):

#		self.object = self.get_object()
#		form = self.get_form()
#		if form.is_valid():
#			form.save()
#			return self.form_valid(form)
#
#	def form_valid(self,form):
		
#		return super(ProfileDetail,self).form_valid(form)
#


def home(request):

	objects = Post.objects.all()
	context={'objects':objects}

	return render(request,'home.html',context)


#def EditProfileForm(request,pk,uuid):
#	profile_data = Profile.objects.get(id=pk)
#	user_form = UserForm(request.POST or None,instance = request.user)
#	form = UpdateProfileForm(request.POST or None,request.FILES,instance=request.user.profile)
#	if form.is_valid() and user_form.is_valid():
#		form.save()
#		user_form.save()
#	context = {'user':request.user,'form':form,'profile_data':profile_data,'user_form':user_form} 	
#
#	return render(request,'blogapp/profile_form.html',context)






def search(request):

	if request.method == "GET":

		search = request.GET.get("search")
		search_datas = Post.objects.all()

		search_results = {

					
			"search":search,
			"search_datas":search_datas

			}
		return render(request,'search.html',search_results)

				
	elif search == None:

		return redirect('/')

	wiki_data = wk.summary(search)
	
	results = 0
	return render(request,"search.html",{"search":search,"results":results,"summary":wiki_data})


#Register function                      
def register(request):


	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get("username")
	

		username_pattern = re.findall("\s",username)


		
		if User.objects.filter(username = username).exists():
			messages.info(request,"Email already exists")
		
		elif  username_pattern:
			messages.info(request,'Not a valid email address')

		elif User.objects.filter(email=username).exists():
			messages.info(request,'Email exists')
				
		else:
			user = User.objects.create_user(first_name=first_name,last_name=last_name,username = username,email = username)
			user.save()
			return redirect('/')
				


	
	return render(request,"register.html")



#Login Function 
#def login(request):

#	if request.method=="POST":
#		login_username = request.POST.get('login_username') 
#		login_password = request.POST.get('login_password')


#		user = auth.authenticate(password=login_password,username=login_username)
		

#		if user is not None and Profile.objects.filter(name=login_username).exists():
#			profile_data = Profile.objects.get(name=login_username)
#			auth.login(request,user)
			

#			return redirect('profile/'+str(profile_data.pk)+"/"+str(profile_data.uuid))
#		else:
#			messages.info(request,"Invalid username or password")



#	return render(request,"login.html")
	
#Logout function     	

#def logout(request):
#	auth.logout(request)
#	return redirect('/')

