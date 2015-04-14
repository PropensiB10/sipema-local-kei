from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)
	role = models.CharField(max_length=15)
	nama_user = models.CharField(max_length=45)

	def __str__(self):
		return "%s " %(self.nama_user)
	
class Jadwal_kelas(models.Model):
	dosen = models.ForeignKey(User)
	hari = models.CharField(max_length=20)
	jammulai = models.TimeField()
	jamselesai = models.TimeField() 
	ruangan = models.CharField(max_length=5)
	class Meta:
		unique_together=(('dosen','hari','jammulai','jamselesai'))
	def __str__(self):
		return " %s \ %s \ %s \ %s \ %s" %(self.dosen.nama_user, self.hari, self.jammulai, self.jamselesai, self.ruangan)

class Order(models.Model):
	waktu_order = models.DateTimeField(auto_now_add = True, auto_now=False) 
	dosen = models.ForeignKey(User, related_name='dosen')
	sekretariat = models.ForeignKey(User, null=True, blank=True, related_name='sekretariat')
		
	def __str__(self):
		return " %s \ %s " %(self.waktu_order, self.dosen.nama_user)
		
class Food(models.Model):
	nama = models.CharField(max_length=100, unique=True)
	total_rating = models.IntegerField(default=0)

	def __str__(self):
		return self.nama
	
class Order_item(models.Model):
	order = models.ForeignKey(Order)
	food = models.ForeignKey(Food)
	qty = models.IntegerField(default=1)
	consumer_type = models.CharField(max_length=20)
	
	def __str__(self):
		return " %s \ %s \ %s \ %s " %(self.order.id, self.order.dosen.nama_user, self.food.nama, self.qty)

class Review(models.Model):
	food = models.ForeignKey(Food)
	rating = models.IntegerField(default=0) 
	komentar = models.CharField(max_length=100, null=True, blank=True)
	dosen = models.ForeignKey(User)
	
	def __str__(self):
		return " %s \ %s \ %s" %(self.food.nama, self.rating, self.komentar)

class Pembayaran(models.Model):
	waktu_bayar = models.DateTimeField(auto_now_add = True, auto_now=False)
	total_pembayaran = models.IntegerField(default=0)
	sekretariat = models.ForeignKey(User) 
	
	def __str__(self):
		return " %s \ %s " %(self.waktu_bayar, self.sekretariat.nama_user)
