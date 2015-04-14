from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import *
from django.template import Context, loader
from .forms import *
#from django.template.context_processors import csrf

def index(request):
	#food_list = Food.objects.all()
	#return HttpResponse("Hello SiPeMa User")
	t = loader.get_template('user-interfaces/home-login.html')
	c = Context('')
	return HttpResponse(t.render(c))
	
def login(request):
	username = 'username'
	password = 'password'
	if request.method == 'POST':
		username2 = request.POST.get('username')
		password2 = request.POST.get('password')
		if usename == username2:
			t = loader.get_template('user-interfaces/m_makanan.html')
			c = Context('')
			return HttpResponse()

def viewfood(request):
	food_list = Food.objects.all()
	t = loader.get_template('user-interfaces/m_makanan.html')
	c = Context({'food_list': food_list,})
	return HttpResponse(t.render(c))
	#return render(request,"user-interfaces/m_makanan.html",food_list)
	#return render(request, "daftarmakanan.html",c)
	
# def addfood(request):
# 	form = FoodForm(request.POST or None)
# 	if form.is_valid():
# 		save_it =  form.save(commit=False)
# 		#konfirmasi dulu mau ditambahin atau engga sebelum disave
# 		save_it.save()
# 	return render_to_response("user-interfaces/daftarmakanan.html", locals(), context_instance=RequestContext(request))
#	return HttpResponseRedirect("user-interfaces/m_makanan.html")

def addfood(request):
	food_list = Food.objects.all()
	form = FoodForm(request.POST or None)
	if 'simpan' in request.POST:
		if form.is_valid():
			save_it =  form.save(commit=False)
			#harusnya ada konfirmasi dulu mau ditambahin atau engga sebelum disave
			nama = form.cleaned_data['nama']
			#new_join, created = Food.objects.filter(nama=nama)
			save_it.save()
			return HttpResponseRedirect('/view/food/')
	#		return list(request, message="Makanan berhasil ditambahkan")
	elif 'batal' in request.POST:
		return HttpResponseRedirect('/view/food/')
	context = {"form":form, 'food_list':food_list}
	template = "user-interfaces/daftarmakanan.html"
	return render(request, template, context)

def deleteFood(request):
	print "masuk deletefood"
	if request.method == 'POST' :
		print request.POST.get("delete")
		food_list2 = Food.objects.filter(id=request.POST.get("delete"))
		print food_list2
		food_list2.delete()
	return HttpResponseRedirect('/add/food/')

def updateFood(request):
	if request.method == 'POST' :
		print request.POST.get("edit")
		food_list2 = Food.objects.filter(id=request.POST.get("edit"))
		print food_list2
		food_list2.update(nama=request.POST.get("nama"))
	return HttpResponseRedirect('/view/food/')	
	
#
def user(request):
	user_list = User.objects.all()
	t = loader.get_template('user-interfaces/p_akun.html')
	a = Context({'user_list': user_list,})
	return HttpResponse(t.render(a))
#

def index2(request):
	context = {}
	template = "index.html"
	return render(request, template, context)
	
def jadwal_kelas(request):
	jadwal_list = Jadwal_kelas.objects.all()
	#return HttpResponse(jadwal_list)
	t = loader.get_template('user-interfaces/j_dosen.html')
	c = Context({'jadwal_list': jadwal_list,})
	return HttpResponse(t.render(c))

def addJadwal(request):
	form = Jadwal_kelasForm(request.POST or None)
	if form.is_valid():
		save_it =  form.save(commit=False)
		save_it.save()
	return render_to_response("addjadwal.html", locals(), context_instance=RequestContext(request))

def addUser(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		save_it =  form.save(commit=False)
		save_it.save()
	return render_to_response("addUser.html", locals(), context_instance=RequestContext(request))


def order(request):
	orderitem_list = Order_item.objects.all() 
	u = loader.get_template('user-interfaces/p_makanan.html')
	b = Context({'orderitem_list': orderitem_list,})
	return HttpResponse(u.render(b))

def addOrder(request):
	form = OrderForm(request.POST or None)
	if form.is_valid():
		save_it =  form.save(commit=False)
		save_it.save()
	return render_to_response("user-interfaces/addorder.html", locals(), context_instance=RequestContext(request))	
		
#UPDATE
#To start, add a URL for form display to urls.py:
#(r'^links/edit/(?P<id>\d+)','test_project.polls.views.edit)
# #Then, to display an HTML edit form in polls/views.py add the following block of code
# def editFood(request,id):
# 	u = Food.objects.get(id=id)
# 	return render_to_response('polls/DaftarMakanan.html',
# 		{'action':'update/' + id,
# 		'button': 'update'})

# #to deal with submitted updates, we add another URL to urls.py:
# #(r'^links/edit/(?P<id>\d+)','test_project.polls.views.update)
# # Finally, we add logic to polls/views.py to add the submitted data then return the list view, passing a message:
# def updateFood(request,id):
# 	u = Food.objects.get(id=id)
# 	u.nama = request.POST["nama"]
# 	u.save()
# 	return list(request, message="Makanan berhasil diubah")

#To support deletion, add a new URL pattern to urls.py:
# #(r'^links/edit/(?P<id>\d+)','test_project.polls.views.delete)
# #Then, to display an HTML edit form in polls/views.py, add the following block of code:
# def deleteFood(request, id):
#	if 'delete' in self.data:
	# 	Food.objects.get(id=id).delete()
	# 	return list(request, message="Makanan berhasil dihapus")