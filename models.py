from django.db import models
from django.forms import ModelForm


class User_Info(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	phone=models.CharField(max_length=12)
	email=models.EmailField(max_length=100)
	password=models.CharField(max_length=100)

	def __str__(self):
		return f'{self.fname} {self.lname} {self.email} {self.phone} {self.password}'

class User_Info_Login(ModelForm):
	class Meta:
		model=User_Info
		fields=['email', 'password']

class User_Info_Signup(ModelForm):
	class Meta:
		model=User_Info
		fields='__all__'