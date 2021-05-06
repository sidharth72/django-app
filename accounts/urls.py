from django.urls import path
from.import views

urlpatterns = [
		
	path('accounts/register',views.register.as_view(),name='register')

]