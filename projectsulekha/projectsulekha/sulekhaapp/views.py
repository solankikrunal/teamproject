from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Signup
import json

# Create your views here.
def signup(request):
	"""View of Signup page we are geting the data from user"""
	""" and post thata data to database"""
	if request.method == "POST":

		if form.is_valid():

			
			email = form.POST.get("email")
			userName = form.POST.get("userName")
			password = form.POST.get("password")
			if 8<= len(password) <=16 and re.search(r'[a-z]',password) and re.search(r'[A-Z]',password) and re.search(r'[0-9]',password) :
				
				uploadData = Signup(first_Name = first_Name, last_Name= last_Name, dateOfBirth = DateOfBirth, gender = gender, email = email, userName = userName, password = password)

				uploadData = uploadData.save()
				return render(request, "success.html")

			else:
				messages.error(request, "invaild password")
				return HttpResponseRedirect ("/sulekha/signup/")

		return render(request, "signup.html")
		
	"""guidance for writing your data in JSON file""" 
	# 	diaplayData =  (serializers.serialize('json',Signup.objects.all()))
	# 	return JsonResponse({'diaplayData':diaplayData})
	# 	with  open("home.json",'a') as test_file:
	# 		 json.dump(displayData, home)

		
	
<<<<<<< HEAD
    

=======
<<<<<<< HEAD
    
=======
    

>>>>>>> master
>>>>>>> rushika
