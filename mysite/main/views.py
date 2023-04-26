from django.shortcuts import render, redirect
from .models import Phone, ContactUs
from django.db.models import Q


from .forms import NewUserForm, ContactForm, PhoneForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    search_post = request.GET.get('search')
    if search_post:    
        phone_list = Phone.objects.filter(Q(name__icontains=search_post) | Q(price__icontains=search_post) | Q(about__icontains=search_post))
    else:
        phone_list = Phone.objects.all()
    return render(request, 'main/index.html', context={
        'phone_list':phone_list})


def about(request):
    return render(request, 'main/about.html')


def index_detail(request, id):
    one_phone = Phone.objects.get(pk=id)

    return render(request, 'main/index_detail.html', context={
        'one_phone':one_phone})



def update_detail(request, id):

    one_phone = Phone.objects.get(pk=id)
    change_name = request.POST.get('name')
    change_price = request.POST.get('price')
    change_about = request.POST.get('about')
    change_img = request.FILES.get('img')

    if request.method == 'POST':
        x = Phone.objects.get(id=id)
        if change_img:
            x.img = change_img
        if change_name:
            x.name = change_name
        if change_price:
            x.price = x.price
        if change_about:
            x.about = change_about
        x.save()
    else:
        one_phone = Phone.objects.get(pk=id)

    return render(request, 'main/update_detail.html', context={
        'one_phone':one_phone})


def delete_detail(request, id):
    one_phone = Phone.objects.get(pk=id)
    if request.method == 'POST':
        x = Phone.objects.get(id=id)
        x.delete()
        return redirect('index')
    else:
        one_phone = Phone.objects.get(pk=id)

    return render(request, 'main/delete_detail.html', context={
       'one_phone':one_phone })


def contact_us(request):
    error = ''
    contactus = ContactUs.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            return redirect('contact_us')
    else:
        error = 'Mi ban sxal a'
    form = ContactForm()
    return render(request,'main/contact_us.html', context={
        'contactus':contactus,
        'error':error
    })



def register_request(request):
	phone_list = Phone.objects.all()
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={
		"register_form":form,
		'phone_list':phone_list,
	})

def login_request(request):
	phone_list = Phone.objects.all()
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={
		"login_form":form,
	    'phone_list':phone_list,
	    'act':'login_request'
        })

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")



def create(request):
    error = ''
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
            # Phone.objects.create(**form.cleaned_data)
                return redirect('index')
        else:
            error = 'Mi ban sxal a'
    form = PhoneForm()

    return render(request, 'main/create.html', context={
        'error': error
        })
