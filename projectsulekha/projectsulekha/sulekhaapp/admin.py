from django.contrib import admin
from .models import SignUP

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']
	class Meta:
		model = SignUP

admin.site.register(SignUP,SignupAdmin)