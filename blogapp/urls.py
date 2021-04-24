from django.urls import path
from.import views
from .views import PostList,PostDetail,ProfileDetail


app_name = 'blogapp'


urlpatterns = [
	
	path('',views.home,name='home'),
	path('newposts',PostList.as_view(),name='postlist'),
	path('newposts/<int:pk>',PostDetail.as_view(),name='postdetail'),
	path('profile/<slug:name>',ProfileDetail.as_view(),name='profiles'),
	path('profile/<slug:name>/newposts',PostList.as_view(),name='postlist'),
	path('login',views.login,name='login'),
	path('register',views.register,name='register'),
	path('profile/<slug:name>/register',views.register,name='register'),	
	path('logout',views.logout,name="logout")

	
]

