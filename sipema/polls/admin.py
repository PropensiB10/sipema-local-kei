from django.contrib import admin

# Register your models here.
from polls.models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ['username','nama_user','role']
	search_fields = ['username','nama_user','role']
	class Meta:
		model = User

class Jadwal_kelasAdmin(admin.ModelAdmin):
	list_display = ['dosen','hari','jammulai','jamselesai','ruangan']
	search_fields = ['dosen','hari','jammulai','jamselesai','ruangan']
	class Meta:
		model = Jadwal_kelas

class FoodAdmin(admin.ModelAdmin):
	list_display = ['nama','total_rating']
	search_fields = ['nama','total_rating'] 
	class Meta:
		model = Food

class OrderAdmin(admin.ModelAdmin):
	list_display = ['waktu_order','dosen','sekretariat']
	search_fields = ['waktu_order','dosen','sekretariat']
	class Meta:
		model = Order

class Order_itemAdmin(admin.ModelAdmin):
	list_display = ['order','food','qty','consumer_type']
	search_fields = ['order','food','qty','consumer_type']
	class Meta:
		model = Order_item

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['food','rating','komentar','dosen']
	search_fields = ['food','rating','komentar','dosen']
	class Meta:
		model = Review

class PembayaranAdmin(admin.ModelAdmin):
	list_display = ['waktu_bayar','sekretariat']
	search_fields = ['waktu_bayar','sekretariat']
	class Meta:
		model = Pembayaran
		
admin.site.register(User, UserAdmin)
admin.site.register(Jadwal_kelas, Jadwal_kelasAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_item, Order_itemAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Pembayaran, PembayaranAdmin)

