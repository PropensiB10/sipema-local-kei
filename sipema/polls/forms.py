from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class FoodForm(forms.ModelForm):
	class Meta:
		model = Food
		fields = ('nama',)

class Jadwal_kelasForm(forms.ModelForm):
	class Meta:
			model = Jadwal_kelas
			fields = ('dosen','hari','jammulai','jamselesai','ruangan')


class UserForm(forms.ModelForm):
	class Meta:
			model = User
			fields = ('username','role','nama_user')

class OrderForm(forms.ModelForm):
	class Meta:			
			model = Order_item			
			fields = ('food','qty','consumer_type')

class updateForm(forms.Form):
 	nama = forms.CharField(max_length=100)









