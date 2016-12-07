from django.contrib import admin
from .models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
	list_display = ['userName','email','password']
	class Meta:
		model = Signup

admin.site.register(Signup,SignupAdmin)