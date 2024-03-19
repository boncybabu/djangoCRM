from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Records


def home(request):
	records = Records.objects.all()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You have been logged in!")
			return redirect('home')
		else:
			messages.success(request,"Error!try again")
			return redirect('home')
	else:
		return render(request,'home.html',{'records':records})



def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
   
def customer_records(request, pk):
	if request.user.is_authenticated:
	    customer_records = Records.objects.get(id=pk)
	    return render(request, 'records.html', {'customer_records':customer_records})
	else:
		messages.success(request,"You must logged in to view that page")
		return redirect('home')

def delete_records(request, pk):
	if request.user.is_authenticated:
		delete_it = Records.objects.get(id=pk)
		delete_it.delete()
		messages.success(request,"Records Deleted Successfully")
		return redirect('home')

	else:
		messages.success(request,"You must be logged in to do that.")
		return redirect('home')

def add_records(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_records = form.save()
				messages.success(request, "Record added..")
				return redirect('home')
		return render(request, 'add_records.html', {'form':form})
	else:
		messages.success(request, "You must be logged in..")
		return redirect('home')


def update_records(request, pk):
	if request.user.is_authenticated:
		current_records = Records.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance= current_records)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has updated")
			return redirect('home')
		return render(request, 'update_records.html', {'form':form})
	else:
		messages.success(request, "You must be logged in..")
		return redirect('home')


