from django.shortcuts import render
from serializers import UserRegister

# Create your views here.

class register(APIView):

	def post(self,request,format=None):

		serializer = UserRegister(data=request.data)

