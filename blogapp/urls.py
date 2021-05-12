from django.urls import path
from.import views
from .views import PostList,PostDetail
from django.contrib.auth.decorators import login_required


app_name = 'blogapp'


urlpatterns = [
	
	path('',views.home,name='home'),
	path('newposts',PostList.as_view(),name='postlist'),
	path('newposts/<slug:slug>',PostDetail.as_view(),name='postdetail'),
	#path('profile/<int:pk>/<uuid:uuid>',login_required(views.ProfileDetail.as_view()),name='profile'),
	#path('login',views.login,name='login'),
	path('register',views.register,name='register'),

	#path('profile/<int:pk>/editprofile/<uuid:uuid>',login_required(views.EditProfileForm),name='editprofile'),	
	#path('logout',views.logout,name="logout"),
	path('search',views.search,name='search'),


	
]
